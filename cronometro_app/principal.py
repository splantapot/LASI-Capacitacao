from prompt_toolkit import choice
from cronometro_app import get_duracao
from cronometro_app.acoes import definir_duracao
from cronometro_app.utilitarios import limpar_tela, get_titulo


# ====== Exibição de menu =====================================================

def gerar_mensagem_menu():
    """Gera a mensagem do menu com a duração atual do cronômetro."""
    return (f"{get_titulo("Cronômetro")}\nDuração atual: {get_duracao()}\nSelecione uma opção:\n")

def exibir_menu():
    """Exibe o menu e seleciona a ação a ser executada."""

    OPCOES_PARADO = [
        (1, "Iniciar cronômetro", lambda: print("Iniciando cronômetro... (função a ser implementada)")),
        (2, "Pausar", lambda: print("Pausando cronômetro... (função a ser implementada)")),
        (3, "Reiniciar", lambda: print("Reiniciando cronômetro... (função a ser implementada)")),
        (4, "Definir tempo", definir_duracao)
        # (5, "Alertar término"),
    ]

    result = choice(
        message=gerar_mensagem_menu(),
        options= [(opcao[0], opcao[1]) for opcao in OPCOES_PARADO],
    )

    print("\n")     # Apenas pelo visual
    OPCOES_PARADO[result-1][2]()  # Chama a função associada à opção selecionada

# ====== Execução principal ===================================================
def executar_app():
    """Executa a aplicação do cronômetro."""
    while True:
        limpar_tela()
        exibir_menu()