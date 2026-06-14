# from calculadora.console import *
from typing import List

maiusculas:List[str] = [chr(i) for i in range(65, 90+1)] # Alfabeto de 'A' a 'Z'
minusculas:List[str] = [chr(i) for i in range(97, 122+1)] # Alfabeto de 'a' a 'z'
#Somei 1 por que o Z não estava sendo incluído

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
    tamanho = len(atuais) # Teoricamente, tamanho = 2**qnt_bits
    if (tamanho & (tamanho - 1)) != 0: return [] # Ex: 100 & 011 = 0 (potência de 2. Falha, caso contrário)
    qnt_bits = (tamanho-1).bit_length() # Conta os bits

    # Início do cálculo
    # Cria uma matriz de "don't cares" (-1) para armazenar os mapas Jn e Kn
    # Cada linha par representa o Jn correspondente / ímpar representa o Kn
    mapas = [[-1 for _ in range(tamanho)] for _ in range(qnt_bits*2)]
    # Executa a função completando Jn e Kn de um dado n de uma só vez
    for bit in range(len(mapas)//2):    # bit: o bit atual (0 = A, 1 = B, ...)
        j = bit*2
        k = (bit*2) + 1
        for num in range(tamanho):  # num: a linha atual da tabela-verdade (0, 1, 2, ...)
            bit_atual = int(bool(atuais[num]&(1<<bit)))     # Captura o bit na posição dada
            bit_prox = int(bool(prox[num]&(1<<bit)))
            caso = (bit_atual<<1)|bit_prox
            # Formata cada comparação como um número: 0 -> 0 = 00, 0 -> 1 = 01, etc.
            # Em cada caso, assimila o valor ao J e K correspondente.
            print(f"{minusculas[bit]}[{num}] : {bit_atual} -> {bit_prox} : [{caso}]")
            match (caso):
                case 0:
                    mapas[j][num] = 0 # Limpa J
                case 1:
                    mapas[j][num] = 1 # Seta J
                case 2:
                    mapas[k][num] = 1 # Seta K
                case 3:
                    mapas[k][num] = 0 # Limpa K
        print(f"J{minusculas[bit]} {[str(v).replace('-1', 'x') for v in mapas[j]]}")
        print(f"K{minusculas[bit]} {[str(v).replace('-1', 'x') for v in mapas[k]]}")

# 00, 01, 10, 11
# 01, 11, 00, 00
estados = [0,1,2,3]
futuros = [1,3,0,0]
# estados = [0,1,2,3,4,5,6,7]
# futuros = [1,3,0,0,0,0,0,0]
obter_expressoes_jk(estados, futuros)