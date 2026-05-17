from typing import List
import datetime

loop = True
def executando():
    """Indica se o cronômetro deve continuar rodando."""
    return loop

def encerrar():
    global loop
    print("Encerrando o cronômetro. Até a próxima!")
    loop = False

# Variável global para armazenar a duração do cronômetro em segundos
DURACAO: List[int,int,int] = [0, 0, 30]  # [horas, minutos, segundos]
    
# Funções de acesso à duração do cronômetro
def get_duracao():
    """Formata a duração do cronômetro para exibição."""
    horas, minutos, segundos = DURACAO
    return f"{horas}:{minutos}:{segundos}"

def get_duracao_list():
    """Retorna a duração do cronômetro como uma lista."""
    return DURACAO

def is_duracao_zero():
    """Verifica se a duração do cronômetro é zero."""
    return DURACAO.count(0) == 3

def set_duracao(horas: int, minutos: int, segundos: int):
    """Define a duração do cronômetro."""
    DURACAO[0], DURACAO[1], DURACAO[2] = horas, minutos, segundos

# Enum de estados do cronômetro
class Estado:
    PARADO = 0
    RODANDO = 1
    PAUSADO = 2
estado_atual = Estado.PARADO  # Estado inicial do cronômetro

# Funções de acesso ao estado
def get_estado():
    return estado_atual

def set_estado(estado):
    global estado_atual
    estado_atual = estado

# Gerenciamento de tempo do cronômetro
tempo_final = datetime.datetime.now()
def get_tempo_final():
    return tempo_final

def set_tempo_final(tempo:datetime.datetime):
    global tempo_final
    tempo_final = tempo

# Gerenciamento de tempo para pausa
inicio_pause = datetime.datetime.now()
def get_inicio_pause():
    return inicio_pause

def set_inicio_pause():
    global inicio_pause
    inicio_pause = datetime.datetime.now()