'''
class data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def displaydata(self):
            print(f"{self.dia:02d}/{self.mes:02d}/{self.ano}")

class datateste:
     def executar_teste():
          data = data(20, 8, 2024)
          data = () #displaydata () não esta se encachando aqui!!!!
datateste.executar_teste()
print
#rever itens
'''

# Classe Data
class Data:
    # Método construtor que inicializa as variáveis de instância
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # Método para exibir a data no formato dd/mm/aaaa
    def displayData(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"

# Aplicativo de teste da classe Data
class DataTeste:
    @staticmethod
    def testar():
        # Criando uma instância da classe Data
        data = Data(26, 8, 2024)
        # Exibindo a data
        print(data.displayData())

# Executando o teste
DataTeste.testar()
