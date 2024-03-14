import random

def jogar_jogo():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")

    while tentativas < max_tentativas:
        print(f"Tentativa {tentativas + 1}/{max_tentativas}")
        palpite = int(input("Digite o seu palpite: "))

        if palpite < numero_secreto:
            print("O número que estou pensando é maior.")
        elif palpite > numero_secreto:
            print("O número que estou pensando é menor.")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas + 1} tentativas!")
            return

        tentativas += 1

    print(f"Você excedeu o número máximo de tentativas. O número secreto era {numero_secreto}.")

if __name__ == "__main__":
    jogar_jogo()
