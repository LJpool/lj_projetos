salario = float(input("Digite o salário do funcionário: "))

desconto = salario * 0.11
if desconto > 318.20:
    desconto = 318.20

print("O desconto previdenciário é de R$", desconto)