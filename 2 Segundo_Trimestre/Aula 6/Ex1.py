class veicolo:
    def __init__(self, Peso = 0, Tanque= 0, Modelo= 0 ):
        self.Peso = float(Peso)
        self.Tanque = float(Tanque)
        self.Modelo = float(Modelo)
    
    def setPeso(self, Peso):
        self.Peso = float(Peso)
    
    def setTanque(self, Tanque):
        self.Tanque = float(Tanque)
    
    def setModelo(self, Modelo):
        self.Modelo = float(Modelo)
    
    def getPeso(self):
        return self.Peso

    def getTanque(self):
        return self.Tanque

    def getModelo(self):
        return self.Modelo

class Terrestre(veicolo):
    def __init__(self, Peso = 0, Tanque= 0, Modelo= 0, Roda= 0):
        super().__init__(Peso , Tanque, Modelo)
        self.Roda = Roda
    
    def setRoda(self, Roda):
        self.Roda = float(Roda)
    
    def getRoda(self):
        return self.Roda
    
class Aereo(veicolo):
    def __init__(self, Peso = 0, Tanque= 0, Modelo= 0, Motor= 0):
        super().__init__(Peso , Tanque, Modelo)
        self.Motor = Motor
    
    def setMotor(self, Motor):
        self.Motor = float(Motor)
    
    def getMotor(self):
        return self.Motor
    
class Aquatico(veicolo):
    def __init__(self, Peso = 0, Tanque= 0, Modelo= 0, Motor= 0):
        super().__init__(Peso , Tanque, Modelo)
        self.Motor = Motor
    
    def setMotor(self, Motor):
        self.Motor = float(Motor)
    
    def getMotor(self):
        return self.Motor