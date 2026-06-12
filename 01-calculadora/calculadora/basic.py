from .console import *

def solicitar_entrada(nome_modo:str, dicas:str, avisos:str) -> None:
    """Escrever os textos explicativos no console"""
    cls()
    prYellow("Tecle 'Ctrl+C' para voltar ao menu.")
    escrever_titulo(f"Modo: {nome_modo}")
    prLightGray(dicas)
    prPurple(avisos)

def soma() -> None:
    """Executa uma soma completa."""
    cls()
    escrever_titulo("Modo: Soma / Subtração")
    solicitar_entrada(
        "Soma",
        "Escreva uma soma algébrica a ser calculada, separados por '+'.\n" +
        "Pressione 'Enter' para realizar o cálculo",
        "Nota: Valores não numéricos serão ignorados.\n" +
        "Espaços nao são obrigatórios. Aceita vírgula.\n" +
        "Exemplo:\n" +
        "2 + 3 + a + nao + 1 - 1 = 2 + 3 + 1 - 1 = 0"
    )
    entrada = input(">>").replace(" ", "").replace(",", ".").replace("-","+-").split("+")
    soma:float = 0
    numeros = []
    for v in entrada:
        try:
            soma += float(v)
        except ValueError: pass #Ignora entrada inválida
    
    print(f"Soma: {soma}")
    input("Tecle 'Enter' para repetir...")
    