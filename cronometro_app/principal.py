from prompt_toolkit import choice
from cronometro_app import get_duracao
from cronometro_app.acoes import definir_duracao
from cronometro_app.utilitarios import limpar_tela, get_titulo


# ====== Exibição de menu =====================================================
def exibir_menu():
    """Exibe o menu e seleciona a ação a ser executada."""

    OPCOES = [
        (1, "Iniciar cronômetro"),
        (2, "Pausar"),
        (3, "Reiniciar"),
        (4, "Definir tempo")
        # (5, "Alertar término"),
    ]

    ACOES = {
        1: lambda: print("Iniciando cronômetro..."),
        2: lambda: print("Pausando cronômetro..."),
        3: lambda: print("Reiniciando cronômetro..."),
        4: definir_duracao,
    }

    result = choice(
        message=
f"""
{get_titulo("Cronômetro")}
Duração atual: {get_duracao()}
Selecione uma opção:
""",
        options=OPCOES,
    )
    print("\n")  # Adiciona uma linha em branco para melhor formatação
    # Obtem e chama a ação correspondente
    ACOES.get(result, lambda: print("Opção inválida"))()

# ====== Execução principal ===================================================
def executar_app():
    """Executa a aplicação do cronômetro."""
    while True:
        limpar_tela()
        exibir_menu()