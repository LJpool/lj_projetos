#4. (2.0) Faça um programa que sorteie um número de 1 a 10 e peça para o usuário tentar adivinhar.
#O usuário tem 3 chances de acertar. Indique se o usuário acertou o errou a cadatentativa.

import random

# Sorteio do número aleatório entre 1 e 10
numero_aleatorio = random.randint(1, 10)

# Número máximo de tentativas permitidas
tentativas_maximas = 3

print("Adivinhe o número entre 1 e 10. Você tem 3 tentativas.")

for tentativa in range(1, tentativas_maximas + 1):
    # Solicitação de entrada do usuário
    palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite: "))
    
    # Verifica se o palpite do usuário está correto
    if palpite == numero_aleatorio:
        print("Parabéns! Você acertou o número.")
        break
    else:
        if tentativa < tentativas_maximas:
            print("Você errou. Tente novamente.")
        else:
            print(f"Você errou. O número correto era {numero_aleatorio}.")
