divisor = int(input("Entre com o valor do divisor: "))

inicio_intervalo = int(input("Início do intervalo: "))
fim_intervalo = int(input("Final do intervalo: "))

divisiveis = []

for numero in range(inicio_intervalo, fim_intervalo + 1):
    if numero % divisor == 0:
        divisiveis.append(numero)

print("Números divisíveis por", divisor, "no intervalo de", inicio_intervalo, "a", fim_intervalo, ":")
print(divisiveis)