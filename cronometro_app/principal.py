import subprocess
import os
from prompt_toolkit import choice
from cronometro_app import OS_WIN, duracao

def limpar_tela():
    """Limpa a tela do terminal."""
    cmd = "cls" if OS_WIN else "clear"
    subprocess.run([cmd], shell=True)

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
        4: lambda: print("Definindo tempo...")
    }

    result = choice(
        message=f"""
=============== MENU ===============
Duração atual: {duracao} segundos
Selecione uma opção:
""",
        options=OPCOES,
    )

    ACOES.get(result, lambda: print("Opção inválida"))()

def executar_app():
    """Executa a aplicação do cronômetro."""
    limpar_tela()
    exibir_menu()