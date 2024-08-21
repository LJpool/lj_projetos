import os

os.system('cls') or None


class Time:
    def __init__(self, hora, minuto, segundo) :
        hora = int(hora)
        minuto= int(minuto)
        segundo = int(segundo)       
       
        if (hora >= 0 and hora < 24):
            self.hora = hora 
        else:
           self.hora = 0
        if (minuto >= 0 and minuto < 60):
            self.minuto = minuto
        else:
           self.minuto = 0
        if (segundo >= 0 and segundo < 60):
            self.segundo = segundo
        else:
           self.segundo = 0
           

    def StringHora24(self):
        print("{}:{}:{}" .format(self.hora, self.minuto, self.segundo))

    def StringHora12(self):
        if(self.hora == 12 or self.hora == 0):
            hora12 = 12
        else:
            hora12 = int(self.hora) % 12        
            print("{}:{}:{}" .format(hora12, self.minuto, self.segundo))

    

if __name__ == "__main__":
    horario = Time(18, 27, 50)
    print(horario.hora)
    horario.StringHora24()
    horario.StringHora12()
    horario2 = Time("9","10","11")
    horario2.StringHora24()
   