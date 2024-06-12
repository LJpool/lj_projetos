def gerar_matriz_identidade(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        matriz[i][i] = 1
        
    return matriz

matriz_identidade_4x4 = gerar_matriz_identidade(4)

print("Matriz identidade 4x4:")
for linha in matriz_identidade_4x4:
    print(' '.join(map(str, linha)))