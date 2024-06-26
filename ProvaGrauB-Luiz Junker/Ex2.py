'''
import random

def gerarToupeiras():
    matriz = [['-' for _ in range(4)] for _ in range(4)] #iniciar a matriz com os 4 buracos vazios
    
    toupeiras_colocadas = 0 #colocar as 4 toupeiras aleatoriamente 
    while toupeiras_colocadas < 4:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        if matriz[i][j] == '-':
            matriz[i][j] = 'T'
            toupeiras_colocadas += 1           
    return matriz

def imprimirMatriz(matriz): #para gerar o ''cenario do jogo''
    for linha in matriz:
        print(" ".join(linha))
    print()

for geracao in range(1, 4): #gerador para imprimir as 3 matrizes
    print(f"Geração {geracao}:")
    matriz = gerarToupeiras()
    imprimirMatriz(matriz)
'''

import random

def gerarToupeiras():
    matriz = [['-' for _ in range(4)] for _ in range(4)] #iniciar a matriz com os 4 buracos vazios
    
    for i in range(4): #colocar as 4 toupeiras aleatoriamente 
        j = random.randint(0, 3)
        matriz[i][j] = 'T'
            
    return matriz

def imprimirMatriz(matriz): #para gerar o ''cenario do jogo''
    for linha in matriz:
        print(" ".join(linha))
    print()

for geracao in range(1, 4): #gerador para imprimir as 3 matrizes
    print(f"Geração {geracao}:")
    matriz = gerarToupeiras()
    imprimirMatriz(matriz)

