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

x, err = determinante([
    [1, -1],
    [1, 6]
])

print(x)