import datetime
import subprocess
import msvcrt

def to_int(valor:str):
    """Tenta converter uma string para inteiro, retornando 0 se falhar."""
    try:
        return int(valor)
    except ValueError:
        return 0

def get_titulo(titulo:str):
    """Retorna um título com '=' para destacar."""
    return f"{'=' * 10} {titulo} {'=' * 10}"

def limpar_tela():
    """Limpa a tela do terminal do Windows."""
    subprocess.run(["cls"], shell=True)

def get_tempo_atual():
    return datetime.datetime.now()

# Função para detectar se o usuário pressionou a tecla Enter para pausar/parar o cronômetro
# Tive que pesquisar
def tecla_pressionada():
    """Verifica se o usuário pressionou uma tecla para pausar/parar (Enter)."""
    # Implementação para Windows
    if msvcrt.kbhit():
        msvcrt.getch()  # Limpa o buffer da tecla
        return True
    return False