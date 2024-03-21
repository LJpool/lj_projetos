# preços dos produtos
preco_camiseta = 25.00
preco_calca = 100.00
preco_cinto = 40.00

# quantidade de cada produto comprado
quantidade_camisetas = int(input("Digite o número de camisetas compradas: "))
quantidade_calcas = int(input("Digite o número de calças compradas: "))
quantidade_cintos = int(input("Digite o número de cintos comprados: "))

# calculando o total da compra
total_compra = (quantidade_camisetas * preco_camiseta) + (quantidade_calcas * preco_calca) + (quantidade_cintos * preco_cinto)

# desconto
desconto = total_compra * 0.10

# aplicando o desconto
total_com_desconto = total_compra - desconto

# valor final da compra
print("O valor do desconto é R$", desconto)
print("O valor da compra com desconto é R$", total_com_desconto)
