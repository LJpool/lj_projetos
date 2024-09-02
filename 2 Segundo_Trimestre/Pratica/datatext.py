'''
Crie uma classe chamada Data que inclui três informações como
variáveis de instância – mês (int), dia (int) e ano (int). Forneça um
método displayData que exibe o dia, o mês e o ano separados por
barras normais ( / ). Escreva um aplicativo de teste chamado
DataTeste que demonstra as capacidades da classe Data. 
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