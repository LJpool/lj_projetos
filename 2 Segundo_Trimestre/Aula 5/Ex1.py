class pessoas:
    def __init__(self, mae, irmas, pai, pessoas):
        self.mae = mae
        self.irmas = irmas
        self.pai = pai
        self.pessoas = pessoas

    def familhas(self):
        if self.pessoas:
            self.familhas = False
        else:
            raise Exception("verificar familhiar")
        
    def liberar(self):
        self.mensagen = True
    
class genetica:
    def __init__(self, nome, afiliação):
        self.nome = nome
        self.afiliação = afiliação
    
    def mostrar_contatos(self):
        return f"genetica: {self.nome}, afiliação: {self.afiliação}"
    
class nomes:
    def __init__(self, antenor, julia, max):
        self.antenor = antenor
        self.julia = julia
        self.max = max
        self.verificar_nomes = self.verificar_nomes()
    
    def verificar_nomes(self):
        return self.pessoas * self.sera_que_ele
    
    def __str__(self):
        return f"Reserva de {self.antenor} no {self.julia}, Total: R${self.total:.2f} para {self.max} dias"