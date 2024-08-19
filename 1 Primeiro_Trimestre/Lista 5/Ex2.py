def tabuada(numero):
    """Recebe um número inteiro e escreve sua tabuada."""
    for i in range(1, 11):
        print("{} x {} = {}".format(numero, i, numero * i))

tabuada(7)