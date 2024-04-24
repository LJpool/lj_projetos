#1. (1.0 pt) Faça uma função que verifique se um número inteiro é primo ou não, retornando: True ou False

def e_primo(num):
    # Verifica se o número é menor ou igual a 1, pois números menores ou iguais a 1 não são primos
    if num <= 1:
        return False
    
    # Verifica se o número é divisível por algum número inteiro de 2 até a raiz quadrada do número + 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    # Se o número não for divisível por nenhum outro número inteiro além de 1 e ele mesmo, então é primo
    return True

# Teste da função
print(e_primo(7))  # Deve retornar True, pois 7 é um número primo
print(e_primo(12)) # Deve retornar False, pois 12 não é um número primo
