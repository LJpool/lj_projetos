nomes = []

for i in range(5):
    nome = input("Digite o {}º nome: ".format(i + 1))
    nomes.append(nome)

nomes.sort()

print("O primeiro nome em ordem alfabética é:", nomes[0])