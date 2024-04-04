from random import randint


posHam1 = 0
posHam2 = 0
#0 - ningem venceu ainda
#1 - ham1 venceu
#2 - ham2 venseu
#3 - empate
vencedor = 0

while vencedor == 0:
    nroSorteado = randint(1,5)
    if nroSorteado == 1:
        posHam1 = posHam1 + 1
    elif nroSorteado == 2:
        posHam1 = posHam1 + 2
    elif nroSorteado == 3:
        pass
    elif nroSorteado == 4:
        posHam1 = posHam1 - 1
    else:
        posHam1 = posHam1 - 2
    if posHam1 < 0:
        posHam1 = 0
        if posHam1 > 12:
            posHam1 = 12

while vencedor == 0:
    nroSorteado = randint(1,5)
    if nroSorteado == 1:
        posHam2 = posHam2 + 1
    elif nroSorteado == 2:
        posHam2 = posHam2 + 2
    elif nroSorteado == 3:
        pass
    elif nroSorteado == 4:
        posHam2 = posHam2 - 1
    else:
        posHam2 = posHam2 - 2
    if posHam2 < 0:
        posHam2 = 0
        if posHam2 > 12:
            posHam2 = 12

    if posHam1 == 12:
        vencedor = 1
    if posHam2 == 12:
        if vencedor == 0:
            vencedor = 2
        else:
            vencedor = 3

    #imprime na tela statos da corida
    print('hamster1: ')
    for n in range(posHam1):
        print('* ', end = ' ')
    print() 
    
#imprime na tela statos da corida
    print('hamster2: ')
    for n in range(posHam2):
        print('* ', end = ' ')
    print() 

if vencedor == 1:
    print('hamster1 venceu')
elif vencedor == 2:
    print('hamster2 vencedor')

