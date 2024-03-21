numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número (divisor): "))

if numero2 != 0:
    resultado = numero1 / numero2
    print("O resultado da divisão é:", resultado)
else:
    print("Erro: divisão por zero!")