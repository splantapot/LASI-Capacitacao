from calculadora.console import *
from typing import List, Tuple, Optional

# Módulo circ_digitais: Circuitos Digitais

# Constantes auxiliares
_INT_DONTCARE:int = -1
_STR_NEGADO:str = "'"
_ALFAMAIUS:List[str] = [chr(i) for i in range(65, 90+1)] # Alfabeto de 'A' a 'Z'
_ALFAMINUS:List[str] = [chr(i) for i in range(97, 122+1)] # Alfabeto de 'a' a 'z'
_DELIMITADORES:List[str] = [".", ",", "-", "/", "\\", ";"]
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

    # Lógica rascunho de simplificação. Funciona bem para 2 bits.
    tamanho, qnt_bits = obter_tamanho_e_bits(tabela)
    if (tamanho < 0 or qnt_bits < 0): return [] # Aborta em caso de erro
    mintermos = [i for i in range(tamanho) if (tabela[i] == 1)] # Calcula mintermos
    for num in mintermos: # Varre procurando os vizinhos
        for bit in range(qnt_bits):
            novo_num = num ^ (1 << bit)
            if (novo_num < len(tabela) and tabela[novo_num] == -1):
                tabela[novo_num] = 1

    
    return [0 if (v == _INT_DONTCARE) else v for v in tabela]

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
                letra = f"{_ALFAMAIUS[bit]}"          # O bit mais à esqueda é o MSB (por exemplo, C em CBA)
                termo = f"{letra}{sinal}{termo}"      # Contrói a expressão A'-> BA'-> C'BA'...
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
                    mapas[k][num] = _INT_DONTCARE # Don't care K
                case 1:
                    mapas[j][num] = 1 # Seta J
                    mapas[k][num] = _INT_DONTCARE # Don't care K
                case 2:
                    mapas[j][num] = _INT_DONTCARE # Don't care J
                    mapas[k][num] = 1 # Seta K
                case 3:
                    mapas[j][num] = _INT_DONTCARE # Don't care J
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

# TESTES

# 00, 01, 10, 11
# 01, 11, 00, 00
# estados = [0,1,2,3]
# futuros = [1,3,0,0]
# estados = [0,1,2,3,4,5,6,7]
# futuros = [1,3,0,0,0,0,0,0]
# expressoes = obter_expressoes_jk(estados, futuros)
# for n in range(len(expressoes)//2):
#     j = n*2
#     k = (n*2)+1
#     print(f"J{_ALFAMINUS[n]}: {expressoes[j]}")
#     print(f"K{_ALFAMINUS[n]}: {expressoes[k]}")

# =========================================================
# Funcões de interação com os usuários
# =========================================================
def solicitar_entrada_contador() -> None:
    """Executa a resolução do contador síncrono."""
    
    i_exec = 0
    bits:int = -1  # Quantidade de bits do contador (número de FFs)
    log_seq_invalida = ""
    log_cic_invalido = ""
    dados_ok = False
    ciclo_ok = False
    contagem:List[int] = []
    estados:List[int] = []
    futuros:List[int] = []

    def construir_secao() -> None:
        nonlocal log_seq_invalida, log_cic_invalido
        cls()
        prYellow("Tecle 'Ctrl+C' para voltar ao menu.")
        escrever_titulo("Modo: Montagem Contador Síncrono", 100)
        prLightGray("Esse modo serve para obter as epressões para um contador síncrono completo.")
        # Validação + exibição de bits
        if ((bits <= 0 and i_exec != 0)):
            prRed("Insira um valor válido.")
        elif log_seq_invalida:
            prRed(f"A sequência inserida é inválida. ({log_seq_invalida})")
            prRed(estados)
            log_seq_invalida = ""
        elif log_cic_invalido:
            prRed(f"O valor inserido é inválido. ({log_cic_invalido})")
            log_cic_invalido = ""
        elif (bits > 0):
            # Não lembrava que o reverse manipulava o ponteiro. Interessante testar.
            bits_simbolos = [_ALFAMAIUS[i] for i in range(bits)]
            bits_simbolos.reverse()
            prGreen(f"Bits: {bits} || MSB {bits_simbolos} LSB")

        if (dados_ok):
            prGreen(f"Contagem: {contagem}")
        if (ciclo_ok):
            prGreen(f"Estados: {estados}")
            prGreen(f"Futuros: {futuros}")


    # Obter Bit
    i_exec = 0
    while bits <= 0:
        construir_secao()
        try:
            print("Insira a quantidade de bits (FFs): ")
            bits = int(input(">>"))
        except ValueError:
            pass
        i_exec+=1

    construir_secao()
    i_exec = 0
    
    # Define o limite numérico máximo com base nos bits (Ex: 3 bits -> limite é 7)
    limite_maximo = (1 << bits) - 1 
    # Solicitar ciclo de contagem
    while not dados_ok:
        construir_secao()
        print('Insira a sequência de contagem (em decimal sem sinal).')
        print(f'Possíveis delimitadores: {" ".join(_DELIMITADORES)}')
        prPurple(f"Ex: {' ; '.join([str(v) for v in range(limite_maximo+1) if (v%2==0) ])} (Números de 0 a {limite_maximo})")
        
        sequencia = input(">>").replace(' ', '')
        
        # Padroniza os delimitadores
        for dl in _DELIMITADORES:
            sequencia = sequencia.replace(dl, _DELIMITADORES[0])
            
        # Obtém lista temporária
        lista_strings = [v for v in sequencia.split(_DELIMITADORES[0]) if v]
        if not lista_strings: #Ignorar lista vazia
            log_seq_invalida = "Lista vazia."
            i_exec += 1
            continue
        contagem_temporaria = []
        log_seq_invalida = ""   # Só pra garantir que venha limpa
        try:
            for caractere in lista_strings:
                v = int(caractere) # Tenta passar para int
                # Valida se está no intervalo de valores
                if v < 0 or v > limite_maximo:
                    log_seq_invalida = "Número fora do escopo de bits"
                    raise ValueError("v invalido")
                if (contagem_temporaria.count(v)):
                    log_seq_invalida = "Repetição de número"
                    raise ValueError("v invalido")
                contagem_temporaria.append(v)
                
        except ValueError:
            log_seq_invalida = "Texto inválido." if not log_seq_invalida else log_seq_invalida
            contagem = lista_strings # Exibição do erro
        else:
            # Se não houver exceção, usaremos os estados válidos para construir as duas listas
            contagem = contagem_temporaria
            
            dados_ok = True
            
        i_exec += 1

    # Novas listas que usaremos
    tamanho_tabela = 2**bits
    novos_estados = [i for i in range(tamanho_tabela)]  # Os novos estados agora estarão em ordem crescente
    novos_futuros = [-1 for _ in range(tamanho_tabela)]

    # Mapeamento base para reaproveitar nas opções de preenchimento automático
    # Cria um dicionário relacionando o estado atual com o futuro
    contagem_futuros = contagem[1:] + [contagem[0]] # Faz lista temporária de futuros da minha contagem
    mapa_ciclo_original = {contagem[i]: contagem_futuros[i] for i in range(len(contagem))}

    if (len(contagem) < tamanho_tabela):
        while not ciclo_ok:
            construir_secao()
            log_cic_invalido = ""

            print("O que deve ser feito com os valores fora do ciclo de contagem?")
            prCyan(f"- Tecle 'Enter' se os valores devem apontar para o valor {contagem[0]}.")
            prCyan("- Digite um número se os valores devem apontar este número específico.")
            prCyan("- Digite 'f' se deseja formatá-los manualmente.")
            
            resposta = input(">> ").replace(" ", "").lower()

            if (not resposta): # Opção 1: Pressionou 'Enter'
                # Percorre o ciclo original completando em cada caso
                for n in range(tamanho_tabela):
                    if n in mapa_ciclo_original:
                        novos_futuros[n] = mapa_ciclo_original[n] # Dentro do ciclo
                    else:
                        novos_futuros[n] = contagem[0] # Destino padrão se estiver fora do ciclo
                
                estados = novos_estados
                futuros = novos_futuros
                ciclo_ok = True

            elif (resposta == "f"): # Opção 2: Inserção manual item por item
                print(f"Estado atual >> Próximo valor (insira)")
                try:
                    for n in range(tamanho_tabela):
                        if n in mapa_ciclo_original:
                            novos_futuros[n] = mapa_ciclo_original[n] # Dentro do ciclo
                        else:
                            # Recebe o novo valor e tenta associá-lo a um futuro adequado
                            val_f = int(input(f"{n} >> "))
                            if val_f < 0 or val_f > limite_maximo:
                                raise ValueError("Fora dos limites")
                            novos_futuros[n] = val_f
                    
                    estados = novos_estados
                    futuros = novos_futuros
                    ciclo_ok = True
                except ValueError:
                    if not log_cic_invalido:
                        log_cic_invalido = f"Operação cancelada. Digite apenas números de 0 a {limite_maximo}."

            else: # Opção 3: Apontar para um número específico
                try:
                    valor = int(resposta)
                    if (valor < 0 or valor > limite_maximo):
                        log_cic_invalido = f"Número fora do escopo de bits (0 a {limite_maximo})."
                    elif (not contagem.count(valor)):
                        log_cic_invalido = "Valor não presente no ciclo."
                    else:
                        # Preenche a tabela apontando os inválidos para este número específico
                        for n in range(tamanho_tabela):
                            if n in mapa_ciclo_original:
                                novos_futuros[n] = mapa_ciclo_original[n]
                            else:
                                novos_futuros[n] = valor
                        
                        estados = novos_estados
                        futuros = novos_futuros
                        ciclo_ok = True
                        
                except ValueError:
                    log_cic_invalido = "Texto inválido." if not log_cic_invalido else log_cic_invalido
    else:
        #Aqui, ordenaremos de maneira crescente
        # Percorre o ciclo original completando em cada caso
        ciclo_ok = True
        for n in range(tamanho_tabela):
            novos_futuros[n] = mapa_ciclo_original[n] # Dentro do ciclo
        estados = novos_estados
        futuros = novos_futuros
    
    construir_secao()

    expressoes = obter_expressoes_jk(estados, futuros)

    if expressoes:
        print("Resolução:")
        for n in range(len(expressoes)//2):
            j = n*2
            k = (n*2)+1
            prYellow(f"J{_ALFAMINUS[n]}: {expressoes[j]}")
            prYellow(f"K{_ALFAMINUS[n]}: {expressoes[k]}")
        
    input("Tecle 'Enter' para repetir...")
        