import random

def gerar_matriz_5x5():
    matriz = [[random.randint(-100, 100) for _ in range(5)] for _ in range(5)]
    return matriz

def transformar_negativos_positivos(matriz):
    for i in range(5):
        for j in range(5):
            matriz[i][j] = -matriz[i][j]

matriz = gerar_matriz_5x5()

print("Matriz original:")
for linha in matriz:
    print(' '.join(map(str, linha)))

transformar_negativos_positivos(matriz)

print("\nMatriz com números negativos transformados em positivos e vice-versa:")
for linha in matriz:
    print(' '.join(map(str, linha)))