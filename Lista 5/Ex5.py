def somar(num1, num2):
    """Soma dois números."""
    return num1 + num2

def subtrair(num1, num2):
    """Subtrai dois números."""
    return num1 - num2

def multiplicar(num1, num2):
    """Multiplica dois números."""
    return num1 * num2

def dividir(num1, num2):
    """Divide dois números. Retorna None se o divisor for zero."""
    if num2 != 0:
        return num1 / num2
    else:
        print("Erro: Divisão por zero.")
        return None

def menu():
    print("Escolha uma operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")

while True:
    menu()
    opcao = int(input("Opção: "))
    if opcao == 0:
        break
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if opcao == 1:
        print("Resultado:", somar(num1, num2))
    elif opcao == 2:
        print("Resultado:", subtrair(num1, num2))
    elif opcao == 3:
        print("Resultado:", multiplicar(num1, num2))
    elif opcao == 4:
        resultado = dividir(num1, num2)
        if resultado is not None:
            print("Resultado:", resultado)