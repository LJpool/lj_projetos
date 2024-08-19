#1. (2.0 pts) Faça uma função divisivelPor2 que receba como parâmetro um número inteiro, e retorne True se o
#número é divisível por 2, e False caso contrário.

def divisivel(num):
    if num %2 == 0:
        return True
    else:
        return False
    
print(divisivel(13)) 
print(divisivel(12)) 