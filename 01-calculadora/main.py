from calculadora.console import *
from typing import List

executando = True   # Variável de controle

def encerrar():
    global executando
    executando = False

opcoes = [
    ["Somar", lambda _: _],
    ["Subtrair", lambda _: _],
    ["Multiplicar", lambda _: _],
    ["Dividir", lambda _: _],
    ["Projetar Contador Sincrono", lambda _: _],
    ["Sair", encerrar],
]

def main():
    try:
        while executando:
            # Aguarda resposta válida
            cls()
            resposta_valida = False
            while not resposta_valida:
                escrever_titulo("Menu")
                opcao = solicitar_opcao([txt for txt, func in opcoes])
                if (opcao == -1):   #Erro: Operação inválida
                    cls()
                    prRed("Erro: Opção não definida no menu.")
                    continue
                elif (opcao == -2): #Erro: Resposta inválida
                    cls()
                    prRed("Erro: Insira uma resposta válida (int).")
                    continue
                resposta_valida = True
            # Executa ação correspondente
            opcoes[opcao-1][1]()

    except KeyboardInterrupt:
        prCyan("\n*Interrupção gerada pelo usuário.")
    finally:
        # Fim
        print("\nVolte sempre!!")
    
if __name__ == "__main__":
    main()