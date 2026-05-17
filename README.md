# Projeto de Capacitação 01 - Cronômetro de Estudos

Projeto desenvolvido durante o processo de capacitação da LASI, executado em maio de 2026.
Desenvolvedor: João Victor (splantapot)

---

## Instruções:

### Objetivo
Criar um cronômetro para sessões de estudo;

### Funcionalidades
- iniciar cronômetro;
- pausar;
- reiniciar;
- definir tempo;
- alertar término;

### Conceitos Trabalhados
- tempo;
- loops;
- controle de execução;

---

# Desenvolvimento

## Como usar

## Lógica de temporização
Pensei na lógica de temporização utilizando timestamp, pois além de não travar o fluxo da aplicação, permite melhor controle do tempo decorrido.

- Definir duração

Definimos a duração em HH:MM:SS

- Iniciar

O timestamp final é armazenado. (TEMPO_FINAL = TEMPO_ATUAL + DURACAO);

- Pausar

O timestamp do início da pausa é salvo. (TEMPO_PAUSE = TEMPO_ATUAL);

- Despausar

O timestamp atual é comparado com o início da pausa, para encontrar a variação de tempo. (DT = TEMPO_ATUAL - TEMPO_PAUSE);
Em seguida, atualiza o timestamp final somando com a variação. (TEMPO_FINAL = TEMPO_FINAL + DT)


## Funcionalidades

## Minhas pesquisas

Eu estava procurando no Google por soluções para fazer um bom aplicativo de console (CLI APP).
Através do [Medium](https://medium.com/@wilson79/10-best-python-cli-libraries-for-developers-picking-the-right-one-for-your-project-cefb0bd41df1), eu encontrei esse tópico que pareceu legal e decidi ler. Então escolhi a biblioteca `prompt_toolkit` para fazer o desenvolvimento, disponível em [https://github.com/prompt-toolkit/python-prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit).

A propósito, neste tópico do [GitHub Docs](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) li sobre a formatação do arquivo .md, que eu não tinha tanto a prática de fazer.
