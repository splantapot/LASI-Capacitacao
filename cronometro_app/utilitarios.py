import subprocess

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