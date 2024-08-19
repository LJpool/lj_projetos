idade_conveniado = int(input("Digite a idade do conveniado: "))

valor_plano = 300

if idade_conveniado < 10:
    valor_plano += 100
elif idade_conveniado <= 30:
    valor_plano += 220
elif idade_conveniado <= 60:
    valor_plano += 395
else:
    valor_plano += 480

print("O valor total a ser pago pelo plano de saúde é R$", valor_plano)