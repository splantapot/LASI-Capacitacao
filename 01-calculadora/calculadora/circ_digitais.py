# from calculadora.console import *
from typing import List, Tuple, Optional

# Módulo circ_digitais: Circuitos Digitais

# Constantes auxiliares
_INT_DONTCARE:int = -1
_STR_NEGADO:str = "'"
_ALFAMAIUS:List[str] = [chr(i) for i in range(65, 90+1)] # Alfabeto de 'A' a 'Z'
_ALFAMINUS:List[str] = [chr(i) for i in range(97, 122+1)] # Alfabeto de 'a' a 'z'
#Somei 1 por que o Z não estava sendo incluído

# Estou tratando tabelas-verdade como listas. Ex:
#  A | S  => S = [1, 0]
#  0 | 1
#  1 | 0

# =========================================================
# Funcões que realizam cálculos
# =========================================================

def obter_tamanho_e_bits(tabela:List[int]) -> Tuple[int,int]:
    tamanho = len(tabela) # Teoricamente, tamanho = 2**qnt_bits
    # Retorna erro se a tabela não é uma potência de 2
    # Ex: 100 & 011 = 0 (potência de 2. Falha, caso contrário)
    if (tamanho & (tamanho - 1)) != 0: return (-1, -1)
    qnt_bits = (tamanho-1).bit_length() #Conta os bits
    return (tamanho, qnt_bits)

def obter_tabela_sem_dontcare(tabela:List[int]) -> List[int]:
    """Remove as condições de dontcare de uma tabela da melhor forma possível.
    
    OBS: A tabela inserida deve estar completa (tamanho == potência de 2)
    """
    tamanho, qnt_bits = obter_tamanho_e_bits(tabela)
    if (tamanho < 0 or qnt_bits < 0): return [] # Aborta em caso de erro
    mintermos = [i for i in range(tamanho) if (tabela[i] == 1)]
    for num in mintermos:
        for bit in range(qnt_bits):
            novo_num = num ^ (1 << bit)
            if (novo_num < len(tabela) and tabela[novo_num] == -1):
                tabela[novo_num] = 1
    nova_tabela = [0 if (v == _INT_DONTCARE) else v for v in tabela]
    return nova_tabela

def obter_expressao_de_tabela(tabela:List[int]) -> Optional[str]:
    """Obtém uma expressão booleana a partir de uma tabela.
        
    OBS: A tabela inserida deve estar completa (tamanho == potência de 2)
    """
    tamanho, qnt_bits = obter_tamanho_e_bits(tabela)
    if (tamanho < 0 or qnt_bits < 0): return None # Aborta em caso de erro
    mintermos = []
    for i in range(tamanho):
        if (tabela[i] == 1):
            termo = ""
            for bit in range(qnt_bits):
                bit_setado = (i&(1<<bit))!=0 # Captura se o bit na posição dada é 1
                sinal = _STR_NEGADO if not bit_setado else ""   # Str para sinal invertido ou não
                termo = f"{_ALFAMAIUS[bit]}{sinal}{termo}"      # Contrói a expressão A'-> BA'-> C'BA'...
            mintermos.append(termo)
    expressao = " + ".join(mintermos) if mintermos else "0"
    return expressao


def obter_expressoes_jk(atuais:List[int], prox:List[int]) -> List[str]:
    """Obtém as expressões dos Flip Flops dado um fluxo de contagem
    É inserido um array com os estados atuais e com os próximos estados.
    O código retorna uma expressão para cada FlipFlop, no formato:
    [Ja, Ka, Jb, Kb, ...] onde A é o LSB
    """
    # Inicialização e validação de erros
    if (not atuais or not prox): return [] # Lista vazia
    if (len(atuais) != len(prox)): return [] # Comprimentos diferentes

    # Quebra a função se o tamanho não é potência de 2
    tamanho, qnt_bits = obter_tamanho_e_bits(atuais) # Conta os bits
    if (tamanho < 0 or qnt_bits < 0): return [] # Aborda em caso de erro

    # Início do cálculo ===================================
    # Cria uma matriz de "don't cares" (-1) para armazenar os mapas Jn e Kn
    mapas = [[_INT_DONTCARE for _ in range(tamanho)] for _ in range(qnt_bits*2)]
    expressoes = ["" for _ in range(qnt_bits*2)]
    for bit in range(len(mapas)//2):    # bit: o bit atual (0 = A, 1 = B, ...)
        # Executa a função completando Jn e Kn de um dado n de uma só vez
        # OBS: posição PAR representa o Jn correspondente / posição ÍMPAR representa o Kn
        j = bit*2
        k = (bit*2) + 1
        for num in range(tamanho):  # num: a linha atual da tabela-verdade (0, 1, 2, ...)
            bit_atual = int(bool(atuais[num]&(1<<bit)))     # Captura o bit na posição dada
            bit_prox = int(bool(prox[num]&(1<<bit)))
            caso = (bit_atual<<1)|bit_prox
            # Formata cada comparação como um número: 0 -> 0 = 00, 0 -> 1 = 01, etc.
            # Em cada caso, assimila o valor ao J e K correspondente.
            # print(f"{minusculas[bit]}[{num}] : {bit_atual} -> {bit_prox} : [{caso}]")
            match (caso):
                case 0:
                    mapas[j][num] = 0 # Limpa J
                case 1:
                    mapas[j][num] = 1 # Seta J
                case 2:
                    mapas[k][num] = 1 # Seta K
                case 3:
                    mapas[k][num] = 0 # Limpa K

        mapas[j] = obter_tabela_sem_dontcare(mapas[j])
        mapas[k] = obter_tabela_sem_dontcare(mapas[k])
        expressoes[j] = obter_expressao_de_tabela(mapas[j])
        expressoes[k] = obter_expressao_de_tabela(mapas[k])
        # Meus prints de depuração
        # print(f"J{_ALFAMINUS[bit]} {[str(v).replace(str(_INT_DONTCARE), 'x') for v in mapas[j]]}")
        # print(f"K{_ALFAMINUS[bit]} {[str(v).replace(str(_INT_DONTCARE), 'x') for v in mapas[k]]}")
        # print(f"J{_ALFAMINUS[bit]} {mapas[j]}")
        # print(f"K{_ALFAMINUS[bit]} {mapas[k]}")
        # print(f"J{_ALFAMINUS[bit]} {expressoes[j]}")
        # print(f"K{_ALFAMINUS[bit]} {expressoes[k]}")
    
    return expressoes

# 00, 01, 10, 11
# 01, 11, 00, 00
estados = [0,1,2,3]
futuros = [1,3,0,0]
estados = [0,1,2,3,4,5,6,7]
futuros = [1,3,0,0,0,0,0,0]
expressoes = obter_expressoes_jk(estados, futuros)
for n in range(len(expressoes)//2):
    j = n*2
    k = (n*2)+1
    print(f"J{_ALFAMINUS[n]}: {expressoes[j]}")
    print(f"K{_ALFAMINUS[n]}: {expressoes[k]}")