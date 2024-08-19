def comparar_palavras(palavra1, palavra2):
    if palavra1 == palavra2:
        print(f"As palavras '{palavra1}' e '{palavra2}' são iguais.")
    elif palavra1 < palavra2:
        print(f"A palavra '{palavra1}' vem antes de '{palavra2}' na ordem alfabética.")
    else:
        print(f"A palavra '{palavra1}' vem depois de '{palavra2}' na ordem alfabética.")

comparar_palavras("banana", "abacaxi")
comparar_palavras("cachorro", "gato")
comparar_palavras("maçã", "maçã")