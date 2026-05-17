from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator
from cronometro_app import set_duracao
from cronometro_app.utilitarios import limpar_tela, get_titulo

# ==========================================
#   Definição de duração
# ==========================================
validacao_horario = Validator.from_callable(
    lambda texto: texto.isdigit() or texto == "",
    error_message="Por favor, digite um número natural ou deixe em branco.",
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
    horas = int(horas) if horas else 0
    minutos = int(minutos) if minutos else 0
    segundos = int(segundos) if segundos else 0

    print(f"\nDuração definida => {horas}h {minutos}m {segundos}s\n")
    confirm = prompt("Confirmar definição? (s/n): ").strip().lower()
    if (confirm == 's'):
        set_duracao(horas, minutos, segundos)