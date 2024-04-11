#funçoes#
def mediaunisinos(grauA, grauB):
    media= (grauA + 2* grauB) / 3.0
    return media 


#principal#

grauA = float(input("digite sua media do grau A: "))
grauB = float(input("digite sua media do grau B: "))

grauFinal = mediaunisinos(grauA, grauB)
print("grau final é: ", grauFinal)