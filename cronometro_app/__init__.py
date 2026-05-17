from typing import List
import datetime

# Variável global para armazenar a duração do cronômetro em segundos
DURACAO: List[int,int,int] = [0, 0, 0]  # [horas, minutos, segundos]
tempo_final = datetime.time(0, 0, 0).isoformat(timespec='seconds')  # Armazena tempo final do cronômetro

def get_duracao():
    """Formata a duração do cronômetro para exibição."""
    horas, minutos, segundos = DURACAO
    return f"{horas}:{minutos}:{segundos}"

def set_duracao(horas: int, minutos: int, segundos: int):
    """Define a duração do cronômetro."""
    DURACAO[0], DURACAO[1], DURACAO[2] = horas, minutos, segundos