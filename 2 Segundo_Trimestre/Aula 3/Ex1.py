#sistema do hotel
class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.disponivel = True
    
    def reservar(self):
        if self.disponivel:
            self.disponivel = False
        else:
            raise Exception("Quarto já reservado")
    
    def liberar(self):
        self.disponivel = True
    
    def __str__(self):
        status = "Disponível" if self.disponivel else "Reservado"
        return f"Quarto {self.numero} ({self.tipo}): {status} - Preço: R${self.preco:.2f}"

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def mostrar_detalhes(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}"

class Reserva:
    def __init__(self, cliente, quarto, dias):
        self.cliente = cliente
        self.quarto = quarto
        self.dias = dias
        self.total = self.calcular_total()
    
    def calcular_total(self):
        return self.dias * self.quarto.preco
    
    def __str__(self):
        return f"Reserva de {self.cliente.nome} no {self.quarto.numero}, Total: R${self.total:.2f} para {self.dias} dias"

class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.quartos = []
    
    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)
    
