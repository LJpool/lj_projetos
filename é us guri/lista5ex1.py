#funçao#
def cumprimentar(nome):
    print("Olá,", nome, "!")


#principal#
nome1 = input("digite seu nome: ")
cumprimentar(nome1)

nome2 = input("usuario 2, digite seu nome: ")
cumprimentar(nome2)

for i in range(5):
    print("usuario", i+1, end = "")
    nome = input(", digite seu nome")
    cumprimentar(nome)