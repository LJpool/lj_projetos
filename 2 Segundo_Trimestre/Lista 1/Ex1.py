'''

usuario = [[0]*6 for _ in range(4)]
usuario[0] = [int(input(f"Valor {i + 1}: ")) for i in range(6)]
usuario[1] = usuario[0][::-1]
usuario[2] = [usuario[0][i] + usuario[1][i] for i in range(6)]

pares = [x for x in usuario[0] if x % 2 == 0]
impares = [x for x in usuario[0] if x % 2 != 0]
usuario[3] = pares + impares + [0] * (6 - len(pares) - len(impares))

print("\nMatriz 1:")
for linha in usuario:
    print("\t".join(map(str, linha)))

print("\nMatriz 2:")
for linha in zip(*usuario):
    print("\t".join(map(str, linha)))
'''

# Criando uma matriz vazia com 4 linhas e 6 colunas
matriz = [[0] * 6 for _ in range(4)]

# Solicitando ao usuário que insira os valores da primeira linha
print("Insira 6 números inteiros para a primeira linha:")
for i in range(6):
    matriz[0][i] = int(input(f"Valor {i+1}: "))

# Segunda linha como a primeira em ordem inversa
matriz[1] = matriz[0][::-1]

# Terceira linha como a soma dos elementos das duas primeiras linhas
for i in range(6):
    matriz[2][i] = matriz[0][i] + matriz[1][i]

# Quarta linha com pares seguidos dos ímpares
pares = [num for num in matriz[0] if num % 2 == 0]
impares = [num for num in matriz[0] if num % 2 != 0]
matriz[3] = pares + impares

# Função para imprimir a matriz
def imprime_matriz(matriz):
    for linha in matriz:
        print("\t".join(map(str, linha)))

print("\nMatriz original:")
imprime_matriz(matriz)

# Criando a transposta da matriz
transposta = list(map(list, zip(*matriz)))

print("\nMatriz transposta:")
imprime_matriz(transposta)

