#3. (2.0) Escreva um trecho de código que verifique e mostre na tela os 10 primeiros números primos.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Inicializando uma lista para armazenar os números primos encontrados
primos_encontrados = []

# Iniciando a busca pelos 10 primeiros números primos
numero = 2  # Começamos com 2, o primeiro número primo
while len(primos_encontrados) < 10:
    if is_prime(numero):
        primos_encontrados.append(numero)
    numero += 1

# Mostrando os 10 primeiros números primos na tela
print("Os 10 primeiros números primos são:")
print(primos_encontrados)
