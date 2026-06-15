from calculadora.console import *

# Módulo basic: Matemática básica

def solicitar_entrada(nome_modo:str, dicas:str, avisos:str) -> None:
    """Escrever os textos explicativos no console"""
    cls()
    prYellow("Tecle 'Ctrl+C' para voltar ao menu.")
    escrever_titulo(f"Modo: {nome_modo}")
    prLightGray(dicas)
    prPurple(avisos)

def solicitar_somar_subtrair() -> None:
    """Executa uma soma/subtração completa."""
    solicitar_entrada(
        "Soma / Subtração",
        "Escreva a expressão a ser calculada, separados por '+' ou '-'.\n" +
        "Pressione 'Enter' para realizar o cálculo",
        "Nota: Valores não numéricos serão ignorados.\n" +
        "Espaços não são obrigatórios. Aceita vírgula.\n" +
        "Exemplo:\n" +
        "2 + 3 + a + nao + 1 - 1 = 2 + 3 + 1 - 1 = 5"
    )
    entrada = input(">>").replace(" ", "").replace(",", ".").replace("-","+-").split("+")
    soma:float = 0
    for v in entrada:
        try:
            if not v:
                continue
            soma += float(v)
        except ValueError: pass #Ignora entrada inválida
    
    print(f"Soma: {soma}")
    input("Tecle 'Enter' para repetir...")

def solicitar_multiplicar_dividir() -> None:
    """Executa uma multiplicação/divisão completa."""
    solicitar_entrada(
        "Multiplicação / Divisão",
        "Escreva expressão a ser calculada, separados por '*' ou '/'.\n" +
        "Pressione 'Enter' para realizar o cálculo",
        "Nota: Valores não numéricos serão ignorados.\n" +
        "'*' ou '/' em sequência (como // ou **) serão contados apenas uma vez (como / e *)\n"
        "Espaços nao são obrigatórios. Aceita vírgula.\n" +
        "Exemplo:\n" +
        "2 * 3 * a * nao * 1*-1 = 2 * 3 * 1 *- 1 = -6"
    )
    entrada = input(">>").replace(" ", "").replace(",", ".")
    eNegativo = False if (entrada.count("-")%2==0) else True
    while (entrada.count('//') or entrada.count('**')):
        entrada = entrada.replace('//','/').replace('**', '*') #Removemos duplicatas
    entrada = entrada.replace("-","").split("*")
    # print(entrada)
    resultado:float = 1
    for exp in entrada:
        try:
            eProduto = True if (exp.count('/') == 0) else False 
            if (eProduto):
                resultado *= float(exp)
            else:
                divisor = 1
                valores = exp.split('/')
                for i in range(len(valores)):  # Pegamos a lista dos valores após o primeiro
                    # Encontramos o divisor total
                    if (i == 0):
                        resultado *= float(valores[i])
                    else:
                        divisor *= float(valores[i])
                print(divisor)
                resultado /= divisor # Fazemos a divisão completa

        except ValueError: pass #Ignora entrada inválida
    if eNegativo:
        resultado *= -1
    print(f"Resultado: {resultado}")
    input("Tecle 'Enter' para repetir...")