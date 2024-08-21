class retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def obter_base(self):
        return self.base 
    
    def obter_altura (self):
        return self.altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return (self.base + self.altura)

retangulo = retangulo(5, 3)
print("base:", retangulo.obter_base())
print("base:", retangulo.obter_altura())
print("base:", retangulo.calcular_area())
print("base:", retangulo.calcular_perimetro())  
    