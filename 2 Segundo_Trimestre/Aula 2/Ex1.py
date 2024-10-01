class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def displayData(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")

# Aplicativo de teste
def DataTeste():
    data = Data(30, 9, 2024)
    data.displayData()

# Executa o teste
DataTeste()
