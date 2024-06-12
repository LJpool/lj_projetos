def verificar_palindromo(palavra):
    palavra = palavra.lower()
    if palavra == palavra[::-1]:
        return True
    else:
        return False

palavras = ["Ana", "osso", "arara", "casa", "python"]
for palavra in palavras:
    if verificar_palindromo(palavra):
        print(f"A palavra '{palavra}' é um palíndromo.")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.")