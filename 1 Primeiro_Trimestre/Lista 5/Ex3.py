def mediaUnisinos(notaA, notaB):
    """Recebe as notas do Grau A e do Grau B e retorna a média final."""
    media = (notaA * 1/3) + (notaB * 2/3)
    return media

media_final = mediaUnisinos(7.5, 8.0)
print("Média final:", media_final)