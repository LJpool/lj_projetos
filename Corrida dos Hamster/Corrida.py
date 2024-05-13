import random
import os

######################FUNÇÕES##############################
def movimentarHamster(posHamster):
    nroSorteado = random.randint(1,5)
    if nroSorteado == 1:
        posHamster = posHamster + 1
    elif nroSorteado == 2:
        posHamster = posHamster + 2
    elif nroSorteado == 3:
        pass
    elif nroSorteado == 4:
        posHamster = posHamster - 1
    else:
        posHamster = posHamster - 2
    if posHamster < 0:
        posHamster = 0
    if posHamster > 12:
        posHamster = 12
    return posHamster

def imprimirStatusCorrida(posHamster1, posHamster2):
    print('Hamster1: ', end = ' ')
    for n in range(posHamster1):
        print('* ', end = ' ')
    print() 

    print('Hamster2: ', end = ' ')
    for n in range(posHamster2):
        print('* ', end = ' ')
    print() 
    print ('-----------------------------------')

def verificarVencedor(posHamster1, posHamster2, vencedor):
    if posHamster1 == 12: 
        vencedor = 1 
    if posHamster2 == 12: 
        if vencedor == 0:
            vencedor = 2 
        else:
            vencedor = 3 
    return vencedor

def imprimirResultadoCorrida(vencedor):
    if vencedor == 1:
        print('Hamster 1 venceu!')
    elif vencedor == 2:
        print('Hamster 2 venceu!')
    else:
        print('Houve um empate!')

################### PROGRAMA PRINCIPAL ########################

posHamster1 = 0
posHamster2 = 0

# 0 - ninguem venceu ainda
# 1 - hamster1 venceu
# 2 - hamster2 venceu
# 3 - empate
vencedor = 0 

while vencedor == 0: 
    os.system('cls' if os.name == 'nt' else 'clear') 
    
   
    posHamster1 = movimentarHamster(posHamster1)

    posHamster2 = movimentarHamster(posHamster2)

    vencedor = verificarVencedor(posHamster1, posHamster2,vencedor)
    
    imprimirStatusCorrida(posHamster1, posHamster2)

imprimirResultadoCorrida(vencedor)