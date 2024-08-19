frase = input("Digite uma frase: ")

quantidade_letras = sum(1 for letra in frase if letra.isalpha())

quantidade_palavras = len(frase.split())

print(f"Quantidade total de letras na frase: {quantidade_letras}")
print(f"Quantidade total de palavras na frase: {quantidade_palavras}")