import subprocess, os
from typing import List

# Função de limpeza
def cls() -> None:
    """Limpar o console."""
    subprocess.run("cls", shell=True)
    # Para linux:
    # subprocess.run("clear", shell=True)

# Funções para escrever colorido
def prRed(s): print("\033[91m {}\033[00m".format(s))
def prGreen(s): print("\033[92m {}\033[00m".format(s))
def prYellow(s): print("\033[93m {}\033[00m".format(s))
def prLightPurple(s): print("\033[94m {}\033[00m".format(s))
def prPurple(s): print("\033[95m {}\033[00m".format(s))
def prCyan(s): print("\033[96m {}\033[00m".format(s))
def prLightGray(s): print("\033[97m {}\033[00m".format(s))
def prBlack(s): print("\033[90m {}\033[00m".format(s))  # Corrected from 98 to 90 (standard ANSI)

# Escrever Título Formatado
def escrever_titulo(titulo:str, tam_linha:int = 20) -> None:
    """Escreve um título no formato indicado em uma linha de tamanho especificado."""
    # tam_linha: Tamanho da linha de um título
    espaco = int((tam_linha-len(titulo))/2)     # Espaçamento para centralizar o título
    print("="*tam_linha)
    print(" "*espaco+titulo)        
    print("="*tam_linha)

# Escrever opções
def solicitar_opcao(opcoes:List[str] = []) -> int:
    """Escreve opções de uma lista. O índice 0 do array será a opção 1.
    Retorna: valor int da opção selecionada.
    Se retornar -1, houve 'erro: opção não listada'
    Se retornar -2, houve 'erro: opção digitada não foi um número'
    """
    for (i, opcao) in enumerate(opcoes):
        print(f"{i+1}. {opcao}")
    resposta = input("Insira uma opção: ")
    try:
        resposta = int(resposta)                        # Tenta converter para int
        if (resposta <= 0 or resposta > len(opcoes)):   # Caso o número respondido seja maior que as opções
            return -1                                   # Erro de opção não listada
        return resposta                                 # Retorna a resposta (se válida)
    except ValueError:
        return -2   # Erro de conversão
    