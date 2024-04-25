#3. (5 pts) Você foi contratado para desenvolver um programa que auxilie um velho alquimista a controlar o
#estoque dos seus ingredientes para preparar suas poções. O programa oferece um menu com 3 opções:
#preparar poção, consultar os ingredientes disponíveis e sair. Se o usuário optar por consultar os ingredientes,
#deve ser listado o nome de cada ingrediente e a quantidade atual de cada um. Tabela 1 mostra os ingredientes
#e suas quantidades iniciais que você deve assumir no programa. Se o usuário optar por preparar poção, você:
#a) Deve pedir para ele o número da poção a ser preparada. Tabela 2 mostra as poções e a quantidade de
#ingredientes que cada uma leva;
#b) Verificar se existe a quantidade de ingredientes suficientes para preparar a poção escolhida. Se não
#houver, você deverá imprimir uma mensagem dizendo qual (ou quais) os ingredientes estão faltando. Se
#tiver todos os ingredientes, você deve descontar essas quantidades dos ingredientes, e imprimir a
#mensagem: poção criada com sucesso! 

ingredientes = {
    "Pó de Fênix": 100,
    "Essência Celestial": 50,
    "Raiz de Dragão": 45,
    "Orvalho Lunar": 30,
    "Flores secas": 200,
    "Elixir amargo": 20,
    "Lágrimas de unicórnio": 15,
}

poçoes = {

    1: {"Poção de Cura": {"Pó de Fênix":30, "Essência Celestial": 20, "Flores Secas": 20, "Lágrimas de unicórnio": 10}},
    2: {"Poção Força da Floresta": {"Orvalho Lunar": 20, "Raiz de Dragão":30, "Flores secas": 30}},
    3: {"Poção Sabedoria da Riqueza": {"Essência Celestial": 30, "Pó de Fênix": 50}},
    4: {"Poção Sorte no Amor": {"Orvalho Lunar": 10, "Flores secas": 50, "Lágrimas de unicórnio": 5}},
    5: {"Poção Malvada": {"Elixir amargo": 10, "Raiz de Dragão": 15}}
}

def consultaringredientes():
    print("ingredientes disponiveis: ")
    for ingrediente, quantidade, in ingredientes.item():
        print(f"{ingrediente}: {quantidade} g/ml")

def prepararpoçao():
    num_poçao = int(input("digite o numero da poçao dezejada: "))
    if num_poçao not in poçoes:
        print("poção não encontrada. ")
        return

    poçao = poçoes[num_poçao]
    faltando = []
    for ingredientes, quantidade in poçao.items():
        if ingredientes.get(ingredientes, 0) < quantidade:
            faltando.append(ingredientes)
    
    if faltando:
        print("igredientes faltando: ")
        for ingredientes in faltando:
             print(ingredientes)
    else:
        for ingredientes, quantidade in poçao.items():
             ingredientes[ingredientes] -= quantidade
        print("poçao criada! ")

while True:
    print("\nMenu:")
    print("1. preparar poçao")
    print("2. consultar ingredientes")
    print("3. sair")
    opçao = input("escolha uma opçao: ")

    if opçao == "1":
        prepararpoçao()
    elif opçao == "2":
        consultaringredientes()
    elif opçao == "3":
        print("saindo... ")
        break
    else:
        print("Opção inválida! ")
