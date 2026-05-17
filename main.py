from cronometro_app.principal import executar_app

def main():
    try:
        executar_app()
    except KeyboardInterrupt:
        print("O usuário encerrou a aplicação.")

if __name__ == "__main__":
    main()