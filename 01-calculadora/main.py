from calculadora.console import *
from calculadora.basic import *
from typing import List

executando = True   # Variável de controle

def encerrar():
    global executando
    executando = False

opcoes = [
    ["Somar/Sutrair", somar_subtrair],
    ["Multiplicar/Dividir", multiplicar_dividir],
    ["Projetar Contador Síncrono", lambda _: _],
    ["Sair", encerrar],
]

def main():
    cls()
    while executando:
        # Aguarda resposta válida
        try:
            resposta_valida = False
            while not resposta_valida:
                escrever_titulo("Menu", 40)
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
            #end while
        except KeyboardInterrupt:
            # O usuário solicitou término da aplicação (Ctrl+C no menu)
            prCyan("\n\n*O usuário interrompeu a aplicação.")
            break

        # Executa ação correspondente
        try:
            while True:
                opcoes[opcao-1][1]()
        except TypeError:
            cls()
            prYellow("Função não especificada no código.") #Bom para depuração
        except KeyboardInterrupt:
            cls()   # A Função chamada solicitou retorno ao menu
        #end try-except
    #end while

    # Fim
    encerrar()  #Boa prática: Garante que o software possua estado encerrado
    print("\nVolte sempre! :)")

    
if __name__ == "__main__":
    main()