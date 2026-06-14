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

def matriz_cofatores(matriz:List[List]) -> Tuple[List[List], int]:
    """Retorna a matriz dos cofatores da matriz dada. Retorna um Tuple: (valor, erro)"""
    ordem = len(matriz)
    if (ordem == 0): return ([], -1)              # Retorna erro -1 se a matriz estiver vazia
    if (ordem != len(matriz[0])): return ([], -2) # Retorna erro -2 se a matriz não for quadrada
    
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

def produto_matriz_escalar(matriz:List[List[float]], escalar:float) -> List[List]:
    """Realiza o produto de uma matriz por um escalar. Retorna a matriz resultante, ou uma matriz vazia em caso de erro."""
    if (not matriz): return []
    return [[elemento * escalar for elemento in linha] for linha in matriz]

# =========================================================
# Funções de interação com o usuário
# =========================================================

def solicitar_entrada_sistema() -> None:
    """Executa a resolução do sistema linear."""
    
    ordem:int = 0  # Ordem do sistema (número de variáveis/equações)
    i_exec:int = 0  # Variável para controlar execução (Usei para controlar o menu e a matriz exibida)
    err_atribuicao = False # Variável que indica erro de atribuição

    def construir_secao() -> None:
        cls()
        prYellow("Tecle 'Ctrl+C' para voltar ao menu.")
        escrever_titulo("Modo: Sistema Linear Quadrado", 100)
        prLightGray("Esse modo serve para calcular a resolução de um Sistema Linear Quadrado.")
        prLightGray("-> (número de icógnitas igual ao número de equações)")
        if (ordem >= 1):
            prGreen(f"Ordem: {ordem}")
            for i in range(ordem):
                prGreen(f"{matriz[i]}     {matriz_resultado[i]}")
        elif (i_exec != 0):
            prRed(f"*A ordem inserida não é válida ({i_exec}).")
        if err_atribuicao:
            prRed("*O valor inserido não foi válido.")

    # Solicita ordem e atualiza a matriz
    while not ordem >= 1:
        construir_secao()
        i_exec += 1 #Aqui, indica quantas vezes o menu apareceu.
        print("Insira a ordem do sistema:")
        try:
            ordem = int(input(">> "))
        except ValueError:
            ordem = -1
        
    matriz:List[List[float]] = [[0 for _ in range(ordem)] for _ in range(ordem)]
    matriz_resultado:List[List[float]] = [[0] for _ in range(ordem)] # Matriz resultado

    i_exec = 0
    while i_exec < ordem**2:
        construir_secao()
        err_atribuicao = False
        j = i_exec%ordem
        i = i_exec//ordem
        print(f"Insira um valor (aceita float) para a posição A[{i}][{j}]:")
        try:
            matriz[i][j] = float(input(">> ").replace(',', '.'))
        except ValueError:
            err_atribuicao = True
        else:
            i_exec += 1 # Incrementa em 1 se o valor foi atribuído corretamente

    i_exec = 0
    while i_exec < ordem:
        construir_secao()
        err_atribuicao = False
        i = i_exec%ordem
        print(f"Insira um valor (aceita float) para a posição R[{i}][0]:")
        try:
            matriz_resultado[i][0] = float(input(">> ").replace(',', '.'))
        except ValueError:
            err_atribuicao = True
        else:
            i_exec += 1 # Incrementa em 1 se o valor foi atribuído corretamente

    construir_secao()
    print("Confirmar matriz? Insira 'r' para redigitar valores.")
    text = input(">> ").lower().replace(' ', '')
    if (text == "r"): 
        # Comentado, pois a minha função de menu já executa em loop
        # solicitar_entrada_sistema()
        return # Quebra a execução

    # Cálculo do sistema
    construir_secao()
    det, err = determinante(matriz)
    if (det == 0):
        prYellow("Sistema indeterminado: Determinante igual a 0.")
    else:
        prYellow(f"Determinante: {det}")
        try:
            inv_det = 1 / det
            matriz_cof, err = matriz_cofatores(matriz)
            matriz_adjunta = matriz_transposta(matriz_cof)
            matriz_inversa = (produto_matriz_escalar(matriz_adjunta, inv_det))
            matriz_final, err = produto_matricial(matriz_inversa, matriz_resultado)
            prYellow("Matriz resultado (x, y, z ...):")
            for linha in matriz_final:
                prYellow(linha)
        except TypeError as e:
            print(e)

    input("Tecle 'Enter' para repetir...")