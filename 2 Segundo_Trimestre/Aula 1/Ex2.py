class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def displayData(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"

class DataTeste:
    @staticmethod
    def testar():
        data = Data(20, 8, 2024)
        print(data.displayData())

DataTeste.testar()
