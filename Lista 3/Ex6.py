import random

aposta = input("Você aposta em PAR ou ÍMPAR? ").upper()

if aposta != "PAR" and aposta != "ÍMPAR":
    print("Opção inválida!")
else:
    numero_usuario = int(input("Digite um número de 0 a 5: "))
    numero_aleatorio = random.randint(0, 5)
    soma = numero_usuario + numero_aleatorio

    print("Número sorteado:", numero_aleatorio)
    print("Soma:", soma)

    if (aposta == "PAR" and soma % 2 == 0) or (aposta == "ÍMPAR" and soma % 2 != 0):
        print("Você venceu!")
    else:
        print("O programa venceu!")