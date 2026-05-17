import datetime
import winsound
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator

from cronometro_app import get_inicio_pause, get_tempo_final, set_duracao, get_duracao_list, is_duracao_zero, set_inicio_pause
from cronometro_app import set_estado, get_estado, Estado, set_tempo_final
from cronometro_app.utilitarios import limpar_tela, get_titulo, to_int, get_tempo_atual

# ==========================================
#   Definição de duração
# ==========================================

validacao_horario = Validator.from_callable(
    lambda texto: (texto.isdigit() or texto == "") and (to_int(texto) < 60),
    error_message="Por favor, digite um número natural menor que 60 ou deixe em branco.",
)

def definir_duracao():
    limpar_tela()
    print(f"{get_titulo('Definir Duração')}\n")

    # Pede que o usuário informe os valores.
    horas = prompt("Digite as horas: ",
        placeholder="0", validator=validacao_horario, validate_while_typing=True)
    minutos = prompt("Digite os minutos: ",
        placeholder="0", validator=validacao_horario, validate_while_typing=True)
    segundos = prompt("Digite os segundos: ",
        placeholder="0", validator=validacao_horario, validate_while_typing=True)
    
    # Converte valores para inteiros ou 0 para entradas vazias.
    horas = to_int(horas) if horas else 0
    minutos = to_int(minutos) if minutos else 0
    segundos = to_int(segundos) if segundos else 0

    print(f"\nDuração definida => {horas}h {minutos}m {segundos}s\n")
    confirm = prompt("Confirmar definição? (s/n): ").strip().lower()
    if (confirm == 's'):
        set_duracao(horas, minutos, segundos)

# ==========================================
#   Inicialização do cronômetro
# ==========================================

def iniciar_cronometro():
    if is_duracao_zero():
        print("Não é possível iniciar o cronômetro com duração zero. Por favor, defina a duração primeiro.")
        prompt("\nPressione Enter para continuar...")
        return
    
    set_estado(Estado.RODANDO)

    # Atualiza o tempo final para o momento de início mais a duração definida
    tempo_atual = get_tempo_atual()
    duracao = get_duracao_list()
    dt = datetime.timedelta(hours=duracao[0]%60, minutes=duracao[1]%60, seconds=duracao[2]%60)
    set_tempo_final(tempo_atual + dt)

def pausar_cronometro():
    if get_estado() == Estado.RODANDO:
        set_estado(Estado.PAUSADO)
        set_inicio_pause()
    elif get_estado() == Estado.PAUSADO:
        set_estado(Estado.RODANDO)
        tempo_atual = get_tempo_atual()
        duracao_pausa = tempo_atual - get_inicio_pause()
        set_tempo_final(get_tempo_final() + duracao_pausa)
    else:
        print("O cronômetro não está rodando. Não é possível pausar.")
        prompt("\nPressione Enter para continuar...")

def encerrar_cronometro():
    set_estado(Estado.PARADO)
    print("Tempo esgotado! Parando o cronômetro.")
    for i in range(16):  # Toca o som 10 vezes
        winsound.Beep(1500+(i%2)*100, 150)  # Frequência de 1500 Hz por 300 ms

    prompt("\nPressione Enter para continuar...")