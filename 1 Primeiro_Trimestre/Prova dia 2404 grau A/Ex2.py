

def divisivelPorN(num1, num2):
    if num2 == 0:
        print("não é posivle dividir por 0")
        return False
    return num1 % num2 == 0
num1 = 10
num2 = 2
print(divisivelPorN(num1, num2))