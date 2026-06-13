# from calculadora.console import *
from typing import List, Tuple

# Módulo algelin: Álgebra Linear

# Funções de interação com o usuário

# Funcões que realizam cálculos
def determinante(matriz:List[List]) -> Tuple[float, int]:
    """Calcula o determinante da matriz dada. Retorna um Tuple: (valor, erro)"""
    ordem = len(matriz)
    if (ordem == 0): return (0, -1)              # Retorna erro -1 se a matriz estiver vazia
    if (ordem != len(matriz[0])): return (0, -2) # Retorna erro -2 se a matriz não for quadrada

    # Prossegue para o cálculo
    valor = 0
    if (ordem == 1):
        valor = matriz[0][0]
    else:
        # Percorre cada coluna
        for coluna in range(ordem):
            sinal = 1 if (coluna%2==0) else -1
            elemento = matriz[0][coluna]
            nova_matriz = [
                [
                    matriz[i][j]
                    for j in range(ordem)
                    if (j != coluna)
                ]
                for i in range(ordem)
                if (i != 0)
            ]
            
            print(matriz)
            det, err = determinante(nova_matriz)
            cofator = det * sinal * elemento
            valor += cofator

    return (valor, 0)

def transposta(matriz:List[List]) -> List[List]:
    """Retorna a matriz transposta da matriz dada."""
    # Retorna uma matriz vazia, caso seja inserida uma matriz vazia
    if (len(matriz) == 0 or len(matriz[0]) == 0): return []

    nova_matriz = [
        [
            matriz[i][j]
            for i in range( len(matriz) )
        ]
        for j in range( len(matriz[0]) )
    ]
    return nova_matriz


def produto_matricial(matrizA:List[List], matrizB:List[List]) -> Tuple[List[List], int]:
    """Calcula o produto matricial entre duas matrizes. Retorna (matriz_produto, err)"""
    if (not matrizA or not matrizB): return ([], -1)   # Erro -1 se alguma matriz não tiver linhas
    linhasA = len(matrizA)
    linhasB = len(matrizB)
    colunasA = len(matrizA[0])
    colunasB = len(matrizB[0])
    if (colunasA * colunasB == 0): return ([], -1)   # Erro -1 se alguma matriz não tiver colunas

    if (colunasA != linhasB): return ([], -2)   # Erro -2, produto incompatível

    nova_matriz = [[0 for _ in range(colunasB)] for _ in range(linhasA)]

    for i in range(linhasA):
        for j in range(colunasB):
            for k in range(colunasA):
                nova_matriz[i][j] += matrizA[i][k]*matrizB[k][j]
    return (nova_matriz, 0)

matrizA = [
    [2, 0],
    [0, 2]
]

matrizB = [
    [1],
    [4]
]


# x, err = determinante([
#     [1, -1],
#     [1, 6]
# ])

for linha in produto_matricial(matrizA, matrizB)[0]:
    print(linha)