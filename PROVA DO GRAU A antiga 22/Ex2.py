#2. (2.0 pts) Faça um programa que leia números inteiros até que o usuário digite 0. No final, 
#imprima a porcentagem de números positivos, negativos, divisíveis por 2, divisíveis por 5 e números primos lidos.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Inicializando as variáveis de contagem
positivos = 0
negativos = 0
divisiveis_por_2 = 0
divisiveis_por_5 = 0
primos = 0
total_numeros = 0

# Loop para ler os números até que o usuário digite 0
while True:
    num = int(input("Digite um número (digite 0 para sair): "))
    if num == 0:
        break

    total_numeros += 1

    # Verificar e atualizar as variáveis de contagem
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    if num % 2 == 0:
        divisiveis_por_2 += 1
    if num % 5 == 0:
        divisiveis_por_5 += 1
    if is_prime(num):
        primos += 1

# Calcular as porcentagens
porc_positivos = (positivos / total_numeros) * 100
porc_negativos = (negativos / total_numeros) * 100
porc_div_2 = (divisiveis_por_2 / total_numeros) * 100
porc_div_5 = (divisiveis_por_5 / total_numeros) * 100
porc_primos = (primos / total_numeros) * 100

# Imprimir os resultados
print(f"Porcentagem de números positivos: {porc_positivos:.2f}%")
print(f"Porcentagem de números negativos: {porc_negativos:.2f}%")
print(f"Porcentagem de números divisíveis por 2: {porc_div_2:.2f}%")
print(f"Porcentagem de números divisíveis por 5: {porc_div_5:.2f}%")
print(f"Porcentagem de números primos: {porc_primos:.2f}%")
