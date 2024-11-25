from math import pi, sqrt

class Forma: #classe base
    def __str__(self):
        return self.__class__.__name__

class FormaBidimensional(Forma): #classe base bidimensionais
    def getArea(self):
        raise NotImplementedError("a subiclase tem que colocar no metodo getArea")

    def desenhar(self):
        raise NotImplementedError("a subiclase tem que ter o metodo de desenhar")

class FormaTridimensional(Forma): #classe base tridimensionais
    def getArea(self):
        raise NotImplementedError("a subiclase tem que colocar no metodo getArea")

    def getVolume(self):
        raise NotImplementedError("a subclase tem que ter o metodo getVolume")

###########formas bidimensional
class circulo(FormaBidimensional):
    def __init__(self, raio, caractere='O'):
        self.raio = raio
        self.caractere = caractere

    def getArea(self):
        return pi * self.raio ** 2

    def desenhar(self):
        for i in range(self.raio):
            print(self.caractere * (self.raio * 2))

class quadrado(FormaBidimensional):
    def __init__(self, lado, caractere='X'):
        self.lado = lado
        self.caractere = caractere

    def getArea(self):
        return self.lado ** 2

    def desenhar(self):
        for _ in range(self.lado):
            print(self.caractere * self.lado)

class triangulo(FormaBidimensional):
    def __init__(self, altura, caractere='A'):
        self.altura = altura
        self.caractere = caractere

    def getArea(self):
        return (self.altura ** 2) / 2

    def desenhar(self):
        for i in range(1, self.altura + 1):
            print(self.caractere * i)

################# formas tridimensional
class esfera(FormaTridimensional):
    def __init__(self, raio):
        self.raio = raio

    def getArea(self):
        return 4 * pi * self.raio ** 2

    def getVolume(self):
        return (4 / 3) * pi * self.raio ** 3

class cubo(FormaTridimensional):
    def __init__(self, lado):
        self.lado = lado

    def getArea(self):
        return 6 * (self.lado ** 2)

    def getVolume(self):
        return self.lado ** 3

class tetraedro(FormaTridimensional):
    def __init__(self, aresta):
        self.aresta = aresta

    def getArea(self):
        return sqrt(3) * (self.aresta ** 2)

    def getVolume(self):
        return (self.aresta ** 3) / (6 * sqrt(2))

##########################aplicaçao
formas = [  
    circulo(3),
    quadrado(3),
    triangulo(4),
    esfera(3),
    cubo(3),
    tetraedro(3)
]

for forma in formas:
    print(f"Classe: {forma}")
    if isinstance(forma, FormaBidimensional):
        print("Tipo: Forma Bidimensional")
        print(f"Área: {forma.getArea()}")
        forma.desenhar()
    elif isinstance(forma, FormaTridimensional):
        print("Tipo: Forma Tridimensional")
        print(f"Área: {forma.getArea()}")
        print(f"Volume: {forma.getVolume()}")
    print()

