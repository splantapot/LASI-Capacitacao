import time, sys
from prompt_toolkit import choice

from cronometro_app import encerrar, executando
from cronometro_app import get_duracao, get_tempo_final, Estado, get_estado
from cronometro_app.acoes import definir_duracao, iniciar_cronometro, pausar_cronometro, encerrar_cronometro

from cronometro_app.utilitarios import get_tempo_atual, limpar_tela, get_titulo, tecla_pressionada

# ====== Exibição de menu =====================================================

def gerar_mensagem_menu():
    """Gera a mensagem do menu com a duração atual do cronômetro."""
    global estado_atual, tempo_final
    return (
        f"{get_titulo("Cronômetro")}"
        f"\nDuração atual: {get_duracao()}"
        f"{f'\nTérmino previsto: {get_tempo_final().strftime('%H:%M:%S')}' if get_estado() != Estado.PARADO else ''}"
        f"{f'\nEstado: {"Rodando" if get_estado() == Estado.RODANDO else "Pausado" if get_estado() == Estado.PAUSADO else "Parado"}' if get_estado() != Estado.PARADO else ''}"
        f"\nSelecione uma opção:"
        # f"\n*Opções indisponíveis\n"
    )

def exibir_menu():
    """Exibe o menu e seleciona a ação a ser executada."""

    OPCOES = [
        (1, "Iniciar cronômetro" if get_estado() == Estado.PARADO else "Reiniciar", iniciar_cronometro),
        (2, "Despausar" if get_estado() == Estado.PAUSADO else "Pausar", pausar_cronometro),
        (3, "Definir tempo", definir_duracao),
        (4, "Testar alerta de término", encerrar_cronometro),
        (5, "Sair", lambda: encerrar()),
        # (5, "Alertar término"),
    ]

    result = choice(
        message=gerar_mensagem_menu(),
        options= [(opcao[0], opcao[1]) for opcao in OPCOES],
    )

    print("\n")     # Apenas pelo visual
    OPCOES[result-1][2]()  # Chama a função associada à opção selecionada

# ====== Exibição do Cronômetro ===============================================
def exibir_cronometro():
    """Exibe o cronômetro em execução atualizando os segundos na tela."""
    limpar_tela()
    print(get_titulo("Cronômetro em Execução"))
    
    # Calcula quanto tempo falta
    tempo_restante = get_tempo_final() - get_tempo_atual()
    
    print(f"\nTempo restante: {tempo_restante} segundos")
    print(f"Término previsto: {get_tempo_final().strftime('%H:%M:%S')}")
    print("\n[Pressione ENTER a qualquer momento para pausar/voltar ao menu]")
    
    # Dorme por 1 segundo dividindo em mini-pausas para verificar o teclado rapidamente
    for _ in range(10):
        time.sleep(0.1)
        if tecla_pressionada():
            pausar_cronometro()  # Altera o estado para PAUSADO, forçando o loop principal a voltar pro menu
            break

# ====== Execução principal ===================================================
def executar_app():
    """Executa a aplicação do cronômetro."""
    while executando():
        limpar_tela()
        if get_estado() == Estado.RODANDO:
            exibir_cronometro()
        else:
            exibir_menu()
        
        if get_estado() == Estado.RODANDO and get_tempo_final() <= get_tempo_atual():
            encerrar_cronometro()

    print("Encerrando o cronômetro. Até a próxima!")