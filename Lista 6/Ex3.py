import random

N = int(input("Digite o número de lançamentos do dado: "))
contagens = [0] * 6

for _ in range(N):
    lance = random.randint(1, 6)  
    contagens[lance - 1] += 1
percentuais = [(contagem / N) * 100 for contagem in contagens]

print("Percentual de ocorrência de cada face do dado:")
for i, percentual in enumerate(percentuais, 1):
    print(f"Face {i}: {percentual:.2f}%")