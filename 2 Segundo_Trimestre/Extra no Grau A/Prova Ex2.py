#adicionei um menu ao sistema 

class Data:
    def __init__(self, dia, mes, ano):
        if self.data_valida(dia, mes, ano):
            self.dia = dia
            self.mes = mes
            self.ano = ano
        else:
            self.dia = 1
            self.mes = 1
            self.ano = 1

    def data_valida(self, dia, mes, ano):  # validar data
        if mes < 1 or mes > 12:
            return False
        if dia < 1 or dia > 31:
            return False
        if mes in [4, 6, 9, 11] and dia > 30:
            return False
        if mes == 2:
            if self.is_bissexto(ano):
                return dia <= 29
            else:
                return dia <= 28
        return True

    def compara(self, outra_data):  # comparar duas datas
        if self.ano > outra_data.ano:
            return 1
        elif self.ano < outra_data.ano:
            return -1
        elif self.mes > outra_data.mes:
            return 1
        elif self.mes < outra_data.mes:
            return -1
        elif self.dia > outra_data.dia:
            return 1
        elif self.dia < outra_data.dia:
            return -1
        else:
            return 0

    def get_dia(self):  # retornar dia
        return self.dia

    def get_mes(self):  # retornar mês
        return self.mes

    def get_mes_extenso(self):  # retornar mês por extenso
        meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
                 "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        return meses[self.mes - 1]

    def get_ano(self):  # retornar ano
        return self.ano

    def is_bissexto(self, ano=None):  # verificar se o ano é bissexto
        if ano is None:
            ano = self.ano
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


#funçoes para o menu

def inserir_data():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
    return Data(dia, mes, ano)

def comparar_datas(data1, data2):
    comparacao = data1.compara(data2)
    if comparacao == 1:
        print("A primeira data é posterior à segunda.")
    elif comparacao == -1:
        print("A primeira data é anterior à segunda.")
    else:
        print("As datas são iguais.")

def exibir_data(data):
    print(f"Data: {data.get_dia()}/{data.get_mes()}/{data.get_ano()}")

def menu():
    data1 = None
    data2 = None

    while True:
        print("\nMenu:")
        print("1. Inserir primeira data")
        print("2. Inserir segunda data")
        print("3. Comparar datas")
        print("4. Exibir mês da primeira data por extenso")
        print("5. Verificar se o ano da primeira data é bissexto")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            data1 = inserir_data()
            print("Primeira data inserida com sucesso!")

        elif opcao == "2":
            data2 = inserir_data()
            print("Segunda data inserida com sucesso!")

        elif opcao == "3":
            if data1 and data2:
                comparar_datas(data1, data2)
            else:
                print("Por favor, insira ambas as datas primeiro.")

        elif opcao == "4":
            if data1:
                print(f"Mês da primeira data por extenso: {data1.get_mes_extenso()}")
            else:
                print("Por favor, insira a primeira data primeiro.")

        elif opcao == "5":
            if data1:
                if data1.is_bissexto():
                    print("O ano da primeira data é bissexto.")
                else:
                    print("O ano da primeira data não é bissexto.")
            else:
                print("Por favor, insira a primeira data primeiro.")

        elif opcao == "6":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu() #executar o menu