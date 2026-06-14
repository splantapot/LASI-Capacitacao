from calculadora.console import *
from typing import List, Tuple

# Módulo algelin: Álgebra Linear

# =========================================================
# Funcões que realizam cálculos
# =========================================================
def determinante(matriz:List[List]) -> Tuple[float, int]:
    """Calcula o determinante da matriz dada. Retorna um Tuple: (valor, erro)"""
    ordem = len(matriz)
    if (ordem == 0): return (1, 0)              # Det de matriz vazia
    if (ordem != len(matriz[0])): return (1, -1) # Retorna erro -1 se a matriz não for quadrada

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
            
            # print(matriz)
            det, err = determinante(nova_matriz)
            cofator = det * sinal * elemento
            valor += cofator

    return (valor, 0)

def matriz_transposta(matriz:List[List]) -> List[List]:
    """Retorna a matriz transposta da matriz dada. Retorna a matriz transposta."""
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

def matriz_cofatores(matriz:List[List]) -> List[List]:
    """Retorna a matriz dos cofatores da matriz dada. Retorna um Tuple: (valor, erro)"""
    ordem = len(matriz)
    if (ordem == 0): return (0, -1)              # Retorna erro -1 se a matriz estiver vazia
    if (ordem != len(matriz[0])): return (0, -2) # Retorna erro -2 se a matriz não for quadrada
    
    # Prossegue para o cálculo

    # Inicializa uma nova matriz
    nova_matriz = [[0 for _ in range(ordem)] for _ in range(ordem)]
    # Percorrendo a nova matriz
    for i in range(ordem):
        for j in range(ordem):
            sinal = 1 if ((i+j)%2==0) else -1
            matriz_reduzida = [
                [ matriz[m][n] for n in range(ordem) if (n != j) ]
                for m in range(ordem) if (m != i)
            ]
            det, err = determinante(matriz_reduzida)
            cofator = det*sinal
            nova_matriz[i][j] = cofator

    return (nova_matriz, 0)

def produto_matricial(matrizA:List[List], matrizB:List[List]) -> Tuple[List[List], int]:
    """Calcula o produto matricial entre duas matrizes. Retorna um Tuple: (matriz_produto, err)"""
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

# =========================================================
# Funções de interação com o usuário
# =========================================================

def solicitar_entrada_sistema() -> None:
    """Executa a resolução do sistema linear."""

    def construir_secao() -> None:
        cls()
        prYellow("Tecle 'Ctrl+C' para voltar ao menu.")
        escrever_titulo("Modo: Sistema Linear Quadrado", 100)
        prLightGray("Esse modo serve para calcular a resolução de um Sistema Linear Quadrado.")
        prLightGray("-> (número de icógnitas igual ao número de equações)")

    variaveis:List[str] = []
    var_validas:bool = False

    while not var_validas:
        construir_secao()
        print("Insira as variáveis (espaçadas por /) ou deixe em branco para inserir a matriz dos coeficientes:")
        texto = input(">> ")
        variaveis = texto.split('/')
        # Verifica se alguma variável é inválida
        var_validas = True
        for v in variaveis:
            if (not v.isalpha()): var_validas = False
        


    input("Tecle 'Enter' para repetir...")