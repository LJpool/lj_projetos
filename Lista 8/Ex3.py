def cebolinha(frase):
    frase_modificada = frase.replace('r', 'l')
    return frase_modificada

frase = input("Digite uma frase: ")
frase_modificada = cebolinha(frase)

print("Frase modificada (Estilo Cebolinha):", frase_modificada)