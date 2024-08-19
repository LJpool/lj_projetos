preco_litro_gasolina = float(input("Digite o preço do litro da gasolina: "))
valor_disponivel = float(input("Digite o valor disponível para abastecer: "))

litros_abastecidos = valor_disponivel / preco_litro_gasolina
print("O motorista conseguiu abastecer", litros_abastecidos, "litros de gasolina.")