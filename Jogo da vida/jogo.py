import random

# Função para simular o lançamento do dado
def lancar_dado():
    return random.randint(1, 6)

# Função para mostrar os números primos até 100
def mostrar_primos():
    primos = []
    for num in range(2, 101):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primos.append(num)
    print("Números primos até 100:", primos)

# Função para fazer o somatório dos números de 1 até 10
def somatorio():
    soma = sum(range(1, 11))
    print("Somatório dos números de 1 até 10:", soma)

# Função para imprimir a série de Fibonacci até o décimo elemento
def fibonacci():
    a, b = 0, 1
    fib = [a, b]
    for _ in range(8):
        a, b = b, a + b
        fib.append(b)
    print("Série de Fibonacci até o décimo elemento:", fib)

# Função para calcular a área de um círculo com raio 2.5
def area_circulo():
    raio = 2.5
    area = 3.14 * (raio ** 2)
    print("Área de um círculo com raio 2.5:", area)

# Função para imprimir o fatorial de 5
def fatorial():
    fat = 1
    for i in range(1, 6):
        fat *= i
    print("Fatorial de 5:", fat)

# Função para imprimir os 5 primeiros números divisíveis por 2 e por 5
def numeros_divisiveis():
    numeros = [num for num in range(1, 21) if num % 2 == 0 and num % 5 == 0][:5]
    print("Os 5 primeiros números divisíveis por 2 e por 5:", numeros)

# Função para executar a ação associada a cada casa do tabuleiro
def acao_jogador(posicao, jogador):
    if posicao == 0:
        print("Você iniciou a jornada!")
    elif posicao == 3:
        print("Desafio matemático!! Escolha uma opção:")
        print("1. Mostrar os números primos até 100")
        print("2. Somar os números de 1 até 10")
        print("3. Imprimir a série de Fibonacci até o décimo elemento")
        print("4. Calcular a área de um círculo com raio 2.5")
        print("5. Imprimir o fatorial de 5")
        print("6. Imprimir os 5 primeiros números divisíveis por 2 e por 5")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            mostrar_primos()
        elif opcao == 2:
            somatorio()
        elif opcao == 3:
            fibonacci()
        elif opcao == 4:
            area_circulo()
        elif opcao == 5:
            fatorial()
        elif opcao == 6:
            numeros_divisiveis()
    # Outras regras associadas às casas do tabuleiro

# Função principal que controla o fluxo do jogo
def jogo_da_vida():
    jogador = 1
    posicao_jogador1 = 0
    posicao_jogador2 = 0
    while True:
        print("Jogador", jogador)
        input("Pressione Enter para girar a roleta...")
        valor_dado = lancar_dado()
        print("Você tirou:", valor_dado)
        if jogador == 1:
            posicao_jogador1 += valor_dado
            print("Você está na casa", posicao_jogador1)
            acao_jogador(posicao_jogador1, jogador)
            if posicao_jogador1 >= 21:
                print("Parabéns! Você venceu!")
                break
            jogador = 2
        else:
            posicao_jogador2 += valor_dado
            print("Você está na casa", posicao_jogador2)
            acao_jogador(posicao_jogador2, jogador)
            if posicao_jogador2 >= 21:
                print("Parabéns! Você venceu!")
                break
            jogador = 1

# Iniciar o jogo
jogo_da_vida()