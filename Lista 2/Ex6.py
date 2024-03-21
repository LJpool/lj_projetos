quantidade_smartphones = int(input("Digite o número de smartphones vendidos: "))
quantidade_tablets = int(input("Digite o número de tablets vendidos: "))

total_smartphones = quantidade_smartphones * 1000.00
total_tablets = quantidade_tablets * 1500.00
total_arrecadado = total_smartphones + total_tablets

print("O total arrecadado com a venda de smartphones é R$", total_smartphones)
print("O total arrecadado com a venda de tablets é R$", total_tablets)
print("O total arrecadado é R$", total_arrecadado)