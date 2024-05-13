import random

valores = []

for _ in range(5):
    valores.append(random.randint(0, 100))

print("Valores sorteados:", valores)

menor_valor = min(valores)
print("Menor valor:", menor_valor)

maior_valor = max(valores)
print("Maior valor:", maior_valor)

media = sum(valores) / len(valores)
print("Média dos valores:", media)