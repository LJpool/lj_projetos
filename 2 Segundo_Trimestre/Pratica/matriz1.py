# Crie uma matriz 4x6, preencha linhas com base na primeira linha dada, e imprima a matriz e sua transposta.

'''
Passo 1: Criar a matriz e solicitar os valores da primeira linha
Primeiro, criamos uma matriz vazia com 4 linhas e 6 colunas, e pedimos ao usuário para inserir os valores da primeira linha.
'''
# Criando uma matriz vazia com 4 linhas e 6 colunas
matriz = [[0] * 6 for _ in range(4)]

# Solicitando ao usuário que insira os valores da primeira linha
print("Insira 6 números inteiros para a primeira linha:")
for i in range(6):
    matriz[0][i] = int(input(f"Valor {i+1}: "))
'''
Passo 2: Preencher a segunda linha com a primeira em ordem inversa
A segunda linha será a primeira em ordem inversa.
'''
# Segunda linha como a primeira em ordem inversa
matriz[1] = matriz[0][::-1]
'''
Passo 3: Calcular a terceira linha como a soma da primeira e segunda
A terceira linha será a soma dos elementos das duas primeiras linhas.
'''
# Terceira linha como a soma dos elementos das duas primeiras linhas
for i in range(6):
    matriz[2][i] = matriz[0][i] + matriz[1][i]
'''
Passo 4: Preencher a quarta linha com pares e ímpares da primeira linha
A quarta linha conterá primeiro os números pares e depois os ímpares da primeira linha.
'''
# Quarta linha com pares seguidos dos ímpares
pares = [num for num in matriz[0] if num % 2 == 0]
impares = [num for num in matriz[0] if num % 2 != 0]
matriz[3] = pares + impares
'''
Passo 5: Imprimir a matriz e sua transposta
Finalmente, imprimimos a matriz original e a transposta, separando as colunas com tabulações (\t).
'''
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

