import subprocess

def get_titulo(titulo:str):
    """Retorna um título com '=' para destacar."""
    return f"{'=' * 10} {titulo} {'=' * 10}\n"

def limpar_tela():
    """Limpa a tela do terminal do Windows."""
    subprocess.run(["cls"], shell=True)