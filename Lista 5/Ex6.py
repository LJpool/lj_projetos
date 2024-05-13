import random

inventario = {"Comum": 0, "Raro": 0, "Lendário": 0}

def abrir_caixa():
    tipo_item = random.choices(["Comum", "Raro", "Lendário"], weights=[80, 19, 1])[0]
    inventario[tipo_item] += 1
    print("Você coletou 1 item {}!".format(tipo_item))

def consultar_itens():
    for tipo, quantidade in inventario.items():
        print("Itens {}: {}".format(tipo, quantidade))

while True:
    print("1 - Abrir uma caixa")
    print("2 - Consultar itens")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        abrir_caixa()
    elif opcao == 2:
        consultar_itens()
    elif opcao == 0:
        break