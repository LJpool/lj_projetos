valor_produto = float(input("Digite o valor do produto: "))

if valor_produto < 20:
    lucro = valor_produto * 0.45
elif valor_produto <= 50:
    lucro = valor_produto * 0.35
else:
    lucro = valor_produto * 0.25

valor_venda = valor_produto + lucro

print("O valor de venda é R$", valor_venda)