import random

def gerar_notas_alunos():
    matriz = []
    for _ in range(10):
        grau_A = round(random.uniform(0.0, 10.0), 1)
        grau_B = round(random.uniform(0.0, 10.0), 1)
        
        grau_parcial = round((grau_A + grau_B) / 2, 1)
        
        matriz.append([grau_A, grau_B, grau_parcial])

    return matriz

matriz_notas = gerar_notas_alunos()

print("Matriz de Notas dos Alunos:")
for linha in matriz_notas:
    print(' '.join(map(str, linha)))