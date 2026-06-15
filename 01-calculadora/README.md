[Voltar](../README.md)

# Projeto de Capacitação 01 - Calculadora Multifuncional

Projeto desenvolvido durante o processo de capacitação da LASI, executado em junho de 2026.
Desenvolvedor: João Victor (splantapot)

## Introdução

O objetivo do projeto era utilizar loops e funções do python para montar uma calculadora que conseguisse executar as operações básicas da matemática (somar, subtrais, multiplicar e dividir) e realizasse duas operações "especiais". As operações especiais escolhidas foram:

- Resolução de Sistema Linear Quadrado
- Montagem de Contador Síncrono Completo

A lógica utilizada para cada uma das operaçoes será detalhada a seguir.

## Funcionamento Geral

O programa consiste basicamente em uma função principal colocada em '''main.py''' chamando funções dos arquivos que desenvolvi para Álgebra Linear ('''algelin.py'''), Circuitos Digitais ('''circ_digitais.py''') e Matemática Básica ('''basic.py'''). O módulo com essas funções se chama '''calculadora.py'''.

No código de main, é possível ver uma lista que associa cada texto de opção do menu a uma função.
O módulo '''console.py''' inclui funçoes de escrita especial no console, formatação e solicitação de entrada.

O aplicativo possui as opções que você deve inserir. Menciona-se que a combinação "Ctrl+C" é usada para encerrar a função atual quando recebida como resposta do usuário. Por exemplo, se você está realizando um cálculo e aperta ctrl+c, encerrará a função matemática atual e retornará ao bloco de código do menu.
Se tornar a usar essa combinação, dessa vez no menu, você fechará a aplicação (solicitação de encerrar o main). Dessa forma, foi fácil navegar entre as funções.

Ao selecionar uma opção, o sistema chama a função associada na lista de opções.
Uma função só pode ser encerrada com a combinação "Ctrl+c".

As funções serão detalhadas a seguir.

## Explicações Lógicas

*OBS: não detalhei a função "encerrar" aqui, pois ela já é autoexplicativa... encerra a aplicação, definindo a variável de controle como "False".

---

### Soma / Subtação (Módulo: Basic)

Inicialmente, pensei em implementar a soma de números A e B quaisquer, mas preferi ampliar a ideia para que o usuário pudesse utilizar quantos valores quisesse, ignorando erros inseridos. Como a soma e a subtração possuem a mesma prioridade matemática e a subtração é basicamente a soma de um número negativo, fica mais fácil implementá-los simultaneamente.

#### Algoritmo
`Entrada: Expressão algébrica contendo somas e subtrações`

`Processamento:`

0. Recebemos a expressão de entrada.
* entrada = 5.9 + 4,1 - 10 + 2 + a
1. Dada a expressão de entrada, todos os espaços vazios são removidos.
* entrada = 5.9+4,1-10+2+a
2. Em seguida, todas as ',' são substituídas por '.' (permitindo float).
* entrada = 5.9+4.1-10+2+a
3. Depois, todos os "-" são substituídos por "+-" (indicando soma com negativo).
* entrada = 5.9+4.1+-10+2+a
4. O código divide todos os termos separados por "+" e gera a lista "entrada"
* entrada = [5.9, 4.1, -10, 2, a] 
5. Iniciamos "soma" como 0.
* soma = 0
6. Então percorremos cada valor da lista "entrada".
Se o valor for um float válido, somamos à soma.
Senão, o ignoramos.
* soma = 5.9 + 4.1 + (-10) + 2 = 2

`Saída: Resultado processado.`

---

### Multiplicação / Divisão (Módulo: Basic)

Pensei de maneira similar à lógica da soma, mas dessa vez para a multiplicação e divisão. O maior cuidado foi com os sinais de divisão e suas repetições.

#### Algoritmo

`Entrada: Expressão algébrica contendo multiplicações e divisões`

`Processamento:`

0. Recebemos a expressão de entrada.
* entrada = 2 * 100 /// 5 // - 5 * 16
1. O filtro de formatação é idêntico ao anterior (espaços e vírgula).
* entrada = 2\*100///5//-5\*16
2. Agora, percorremos um loop para tirar barras e asteriscos duplos
* entrada = 2\*100/5/-5\*16
3. E então um caso que remove os sinais negativos e define o sinal da expressão final.
* entrada = 2\*100/5/5\*16     || expressão: negativa
4. Dividimos os temos nos asteriscos, e definimos resultado como 1
* entrada = [2, 100/5/5, 16] || resultado = 1
5. Verificamos se o próximo número é um número ou uma divisão
Se número: calcula produto e prossegue
Se divisão:
- Dividimos novamente, dessa vez por cada barra.
* entrada = [2, [100, 5, 5], 16]
- Multiplicamos o resultado pelo primeiro termo e dividimos pelo produto dos demais. Assim encontramos um valor completo, para prosseguirmos repetindo os passos 4 e 5
* entrada = [2, 4, 16]
6. Temos o resultado e o sinal
* resultado = -128 (sinal negativo)

`Saída: Resultado processado.`

---

### Projetar Contador Síncrono

Eu queria muito desenvolver esse projeto por causa das minhas experiências projetando contadores.
A parte de projetar as tabelas das expressões Jn e Kn, considerando que n é o número do n-ésimo FlipFlop (FF), foi simples: tendo um fluxo de contagem organizado, facilmente você consegue produzir uma tabela com as condições verdadeiras e as condições de "Don't care". O problema, inclusive é o que eu gostaria de ter resolvido, é garantir que encontraremos a expressão mais simplificada para os valores J e K correspondentes.
Para garantir isso, eu teria que estudar o método do tabulamento, que não era o intuito da capacitação. Então coloquei uma lógica inspirada no Mapa K que funciona muito bem para contadores pequenos, mas não cheguei a testar com muitos bits.

#### Algoritmo

`Entrada: Qnt de bits e o fluxo de contagem (completo, incluindo casos omitidos)`

`Processamento:`

1. Recebemos (e validamos) a quantidade de bits.
* bits = 2
2. Recebemos o ciclo de contagem
* contagem = [00, 01, 11]
3. Organizamos o fluxo de contagem como uma matriz chamada estados e os estados subsequentes como a matriz "futuro". Note que os casos omissos em "contagem" também são incluídos aqui
estados = [00, 01, 10, 11]
futuros = [01, 11, 00, 00]
3. Depois, sistema irá gerar um matriz, contendo as n tabelas para J e K de cada FF. Os Jn serão os índices pares e os Kn serão os ímpares. Os "dontcare" são representados por -1
tabelas = [Ja, Ka, Jb, Kb, Jc, Kc]
4. Executamos um algoritmo simples para substiruir  "Don't care" vizinhos a 1 por x (por isso fica bom com 2 bits, já que simplificar o vizinho sempre gera um par)
5. Substituímos os casos não modificados por 0
6. Retornamos ao usuário as expressões das tabelas sem o dontcare.

`Saída: Resultado processado.`

---

### Resolver Sistema Linear Quadrado

Pensei no sistema linear quadrado pois ele é facilmente resolvível com uma equação algébrica, que é um conjunto de várias funções algébricas. Um sistema linear não quadrado fica mais fácil de ser resolvido por escalonamento, mas não tive nenhuma ideia direta para esse método.

Se temos um sistema A x X = B
Então temos a solução
X = A' x B
Onde A' é a matriz inversa, dada por
A' = 1/detA * adj(A)      (A matriz adjunta é a transposta da matriz dos cofatores)

#### Algoritmo

`Entrada: Ordem N da matriz e valores da matriz`

`Processamento:`

1. Recebemos (e validamos) a ordem da matriz.
* ordem = input()
2. Solicitamos aos usuários os valores em sequência para cada posição da matriz dos coeficientes.
3. Depois, o usuário deve inserir a matriz dos resultados.
4. Executamos a álgebra listada acima, isolando X.
5. Exibimos o valos da matriz X, caso ela possua inversa.

`Saída: Resultado processado.`

---

## Links externos:

[Colocar cores no console.](https://www.geeksforgeeks.org/python/print-colors-python-terminal/)