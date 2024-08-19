vetor = []

for i in range(5):
    valor = int(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)
resultado = [valor * i for i, valor in enumerate(vetor)]

print("Resultado da multiplicação de cada valor pela sua posição:")
print(resultado)