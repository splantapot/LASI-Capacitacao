import datetime

# Variável global para armazenar a duração do cronômetro em segundos
duracao = datetime.time(0, 0, 0).isoformat(timespec='seconds')

# Enum para estado do cronometro
class Estado:
    PARADO = 0
    RODANDO = 1
    PAUSADO = 2

estado_atual = Estado.PARADO

# Funções para manipular a duração do cronômetro

def get_duracao():
    """Formata a duração do cronômetro para exibição."""
    global duracao
    horas, minutos, segundos = duracao.split(':')
    return f"{horas}:{minutos}:{segundos}"

def set_duracao(horas: int, minutos: int, segundos: int):
    """Define a duração do cronômetro."""
    global duracao
    duracao = datetime.time(horas, minutos, segundos).isoformat(timespec='seconds')