import random

def gerar_matriz_4x6():
    matriz = [[random.randint(-10, 10) for _ in range(6)] for _ in range(4)]
    return matriz

matriz = gerar_matriz_4x6()

print("Matriz 4x6:")
for linha in matriz:
    print(' '.join(map(str, linha)))

maior_valor = float('-inf')  
menor_valor = float('inf')   

for linha in matriz:
    for elemento in linha:
        if elemento > maior_valor:
            maior_valor = elemento
        if elemento < menor_valor:
            menor_valor = elemento

print(f"\nO maior valor da matriz é: {maior_valor}")
print(f"O menor valor da matriz é: {menor_valor}")