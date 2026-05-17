from prompt_toolkit import choice
from cronometro_app import get_duracao
from cronometro_app.acoes import definir_duracao
from cronometro_app.utilitarios import limpar_tela, get_titulo


# ====== Exibição de menu =====================================================
def exibir_menu():
    """Exibe o menu e seleciona a ação a ser executada."""

    OPCOES_PARADO = [
        (1, "Iniciar cronômetro", lambda: print("Iniciando cronômetro...")),
        (2, "Pausar", lambda: print("Pausando cronômetro...")),
        (3, "Reiniciar", lambda: print("Reiniciando cronômetro...")),
        (4, "Definir tempo", definir_duracao)
        # (5, "Alertar término"),
    ]

    ACOES = {
        0: lambda: print("Iniciando cronômetro..."),
        1: lambda: print("Pausando cronômetro..."),
        2: lambda: print("Reiniciando cronômetro..."),
        3: definir_duracao,
    }

    result = choice(
        message=
f"""
{get_titulo("Cronômetro")}
Duração atual: {get_duracao()}
Selecione uma opção:
""",
        options= [(opcao[0], opcao[1]) for opcao in OPCOES_PARADO],
    )
    print("\n")
    OPCOES_PARADO[result-1][2]()  # Chama a função associada à opção selecionada

# ====== Execução principal ===================================================
def executar_app():
    """Executa a aplicação do cronômetro."""
    while True:
        limpar_tela()
        exibir_menu()