import random

quantidade_faces = int(input("Digite a quantidade de faces do dado (4, 6, 8, 10, 12 ou 16): "))

if quantidade_faces not in [4, 6, 8, 10, 12, 16]:
    print("Quantidade de faces inválida!")
else:
    
    numero_sorteado = random.randint(1, quantidade_faces)
    print("O número sorteado é:", numero_sorteado)