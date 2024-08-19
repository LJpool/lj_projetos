def calcular_fatorial(numero):
    """Calcula o fatorial de um número inteiro positivo."""
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

while True:
    num = int(input("Entre com um número para calcular o fatorial: "))
    
    if num < 0:
        print("Número inválido. O número deve ser maior ou igual a zero.")
        continue
    
    resultado = calcular_fatorial(num)
    print("O fatorial de", num, "é", resultado)
    
    continuar = input("Calcular outro número (s/n)? ").lower()
    if continuar != 's':
        break