valor_saque = int(input("Digite o valor a ser sacado: "))

notas = [100, 50, 20, 10, 5, 1]

quantidade_notas = {}

for nota in notas:
    quantidade_notas[nota] = valor_saque // nota
    valor_saque %= nota

print("Notas utilizadas:")
for nota, quantidade in quantidade_notas.items():
    if quantidade > 0:
        print(quantidade, "nota(s) de R$", nota)