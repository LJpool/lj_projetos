import csv
from datetime import datetime

class ONGAdoteGatinhos:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = self.load_data()

    def load_data(self):
        data = []
        try:
            with open(self.file_name, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
            return data
        except FileNotFoundError:
            print("Arquivo CSV não encontrado.")
            return []

    def save_data(self):
        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(self.data)
        print("Dados salvos com sucesso.")

    def menu(self):
        while True:
            print("\nMenu Principal:")
            print("1) Cadastrar felino")
            print("2) Alterar status de felino")
            print("3) Consultar informações sobre felino")
            print("4) Apresentar estatísticas gerais")
            print("5) Filtragem de dados")
            print("6) Salvar")
            print("7) Sair do programa")

            option = input("Escolha uma opção: ")

            if option == "1":
                self.cadastrar_felino()
            elif option == "2":
                self.alterar_status_felino()
            elif option == "3":
                self.consultar_felino()
            elif option == "4":
                self.apresentar_estatisticas()
            elif option == "5":
                self.filtrar_dados()
            elif option == "6":
                self.save_data()
            elif option == "7":
                self.save_data()
                break
            else:
                print("Opção inválida. Tente novamente.")

    def cadastrar_felino(self):
        print("\nCadastrar novo felino:")
        felino = {}
        felino['Nome'] = input("Nome: ")
        felino['Sexo'] = input("Sexo (M/F): ")
        felino['Idade'] = input("Idade: ")
        felino['Raça'] = input("Raça: ")
        felino['Cor Predominante'] = input("Cor Predominante: ")
        felino['Castrado'] = input("Castrado (Sim/Não): ")
        felino['FIV+'] = input("FIV+ (Sim/Não): ")
        felino['FELV+'] = input("FELV+ (Sim/Não): ")
        felino['Data de Resgate'] = input("Data de Resgate (dd/mm/yyyy): ")
        felino['Adotado'] = input("Adotado (Sim/Não): ")
        felino['Lar Temporário'] = input("Lar Temporário (Sim/Não): ")
        felino['Data de Adoção/Hospedagem'] = input("Data de Adoção/Hospedagem (dd/mm/yyyy): ")
        felino['Tutor'] = input("Tutor: ")
        felino['Contato'] = input("Contato: ")
        felino['Data da Última Vacina'] = input("Data da Última Vacina (dd/mm/yyyy): ")
        felino['Data da Última Desvermifugação'] = input("Data da Última Desvermifugação (dd/mm/yyyy): ")
        felino['Data do Último Antipulgas'] = input("Data do Último Antipulgas (dd/mm/yyyy): ")
        felino['Informações Extras'] = input("Informações Extras: ")

        self.data.append(felino)

    def alterar_status_felino(self):
        print("\nAlterar status de felino:")
        for idx, row in enumerate(self.data):
            print(f"{idx}: {row['Nome']}")
        
        idx = int(input("Escolha o felino pelo número: "))
        if 0 <= idx < len(self.data):
            felino = self.data[idx]
            print(f"\nAlterar informações de {felino['Nome']}:")
            for i, (key, value) in enumerate(felino.items()):
                print(f"{i+1}) {key}: {value}")

            while True:
                field = input("Escolha o campo que deseja alterar (ou 'sair' para terminar): ")
                if field == 'sair':
                    break
                elif field.isdigit() and 1 <= int(field) <= len(felino):
                    field_name = list(felino.keys())[int(field)-1]
                    new_value = input(f"Novo valor para {field_name}: ")
                    self.data[idx][field_name] = new_value
                else:
                    print("Campo inválido. Tente novamente.")
        else:
            print("Felino não encontrado.")

    def consultar_felino(self):
        print("\nConsultar informações sobre felino:")
        for idx, row in enumerate(self.data):
            print(f"{idx}: {row['Nome']}")
        
        idx = int(input("Escolha o felino pelo número: "))
        if 0 <= idx < len(self.data):
            felino = self.data[idx]
            print(f"\nInformações sobre {felino['Nome']}:")
            for key, value in felino.items():
                print(f"{key}: {value}")
        else:
            print("Felino não encontrado.")

    def apresentar_estatisticas(self):
        print("\nEstatísticas gerais:")
        total = len(self.data)
        if total > 0:
            machos = sum(1 for felino in self.data if felino['Sexo'] == 'M')
            femeas = sum(1 for felino in self.data if felino['Sexo'] == 'F')
            adotados = sum(1 for felino in self.data if felino['Adotado'] == 'Sim')
            nao_adotados = total - adotados
            fiv_felv = {
                ('Sim', 'Sim'): 0,
                ('Sim', 'Não'): 0,
                ('Não', 'Sim'): 0,
                ('Não', 'Não'): 0
            }
            for felino in self.data:
                fiv_felv[(felino['FIV+'], felino['FELV+'])] += 1

            print(f"Porcentagem de machos: {machos / total * 100:.2f}%")
            print(f"Porcentagem de fêmeas: {femeas / total * 100:.2f}%")
            print(f"Porcentagem de adotados: {adotados / total * 100:.2f}%")
            print(f"Porcentagem de não adotados: {nao_adotados / total * 100:.2f}%")
            print("\nPorcentagem de felinos testados para FIV e FELV:")
            for key, count in fiv_felv.items():
                print(f"FIV: {key[0]}, FELV: {key[1]} -> {count / total * 100:.2f}%")
        else:
            print("Nenhum dado disponível para estatísticas.")

    def filtrar_dados(self):
        print("\nFiltragem de dados:")
        print("1) Consultar gatos resgatados por período")
        print("2) Consultar gatos adotados por período")
        option = input("Escolha uma opção: ")

        if option == "1":
            ano_inicio = int(input("Ano de início: "))
            ano_fim = int(input("Ano de fim: "))
            resgatados = [felino for felino in self.data if ano_inicio <= datetime.strptime(felino['Data de Resgate'], "%d/%m/%Y").year <= ano_fim]
            print(f"\nGatos resgatados de {ano_inicio} a {ano_fim}:")
            for felino in resgatados:
                print(felino)
        elif option == "2":
            ano_inicio = int(input("Ano de início: "))
            ano_fim = int(input("Ano de fim: "))
            adotados = [felino for felino in self.data if ano_inicio <= datetime.strptime(felino['Data de Adoção/Hospedagem'], "%d/%m/%Y").year <= ano_fim]
            print(f"\nGatos adotados de {ano_inicio} a {ano_fim}:")
            for felino in adotados:
                print(felino)
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    ong = ONGAdoteGatinhos("gatinhos.csv")
    ong.menu()
    