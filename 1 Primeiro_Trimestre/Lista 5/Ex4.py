import random

def sorteio(inicio, fim):
    """Recebe um intervalo de valores inteiros [inicio, fim] e sorteia um número dentro desse intervalo."""
    return random.randint(inicio, fim)

num_sorteado = sorteio(1, 100)
print("Número sorteado:", num_sorteado)