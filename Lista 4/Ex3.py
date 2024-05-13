numero = int(input("Entre com um número de 1 a 9: "))

if numero < 1 or numero > 9:
    print("Número inválido. Por favor, entre com um número de 1 a 9.")
else:
    print("Tabuada de multiplicação de", numero, ":")
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)