import random

def gerar_matriz_4x6():
    matriz = [[random.randint(-10, 10) for _ in range(6)] for _ in range(4)]
    return matriz

matriz = gerar_matriz_4x6()

print("Matriz 4x6:")
for linha in matriz:
    print(' '.join(map(str, linha)))

soma_segunda_linha = sum(matriz[1])
soma_quinta_coluna = sum(linha[4] for linha in matriz)
soma_multiplicacao_primeira_quarta_linha = sum(matriz[0][i] * matriz[3][i] for i in range(6))
soma_colunas_pares = sum(linha[i] for linha in matriz for i in range(6) if i % 2 == 0)
soma_linhas_impares = sum(matriz[i][j] for i in range(4) for j in range(6) if i % 2 != 0)

print("\nResultados das somas:")
print(f"Soma dos elementos da segunda linha: {soma_segunda_linha}")
print(f"Soma dos elementos da quinta coluna: {soma_quinta_coluna}")
print(f"Soma da multiplicação dos elementos da primeira linha pelos elementos da quarta linha: {soma_multiplicacao_primeira_quarta_linha}")
print(f"Soma dos elementos das colunas com índices pares: {soma_colunas_pares}")
print(f"Soma dos elementos das linhas com índices ímpares: {soma_linhas_impares}")