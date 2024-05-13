import random

numero_sorteado = random.randint(1, 10)

tentativas = 3

while tentativas > 0:
    tentativa = int(input("Tentativa (restam {}): ".format(tentativas)))

    if tentativa == numero_sorteado:
        print("Parabéns! Você acertou o número!")
        break
    elif tentativa < numero_sorteado:
        print("O número sorteado é maior.")
    else:
        print("O número sorteado é menor.")
    
    tentativas -= 1

if tentativas == 0:
    print("Você perdeu! O número sorteado era:", numero_sorteado)