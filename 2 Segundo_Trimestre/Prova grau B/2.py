class Ingresso: #classe base 
    def __init__(self, valor, localizacao):
        self.valor = valor
        self.localizacao = localizacao

    def imprimeValor(self):
        print(f"Valor do ingresso: R$ {self.valor:.2f}")

    def imprimeLocalizacao(self):
        print(f"Localização: {self.localizacao}")
###########tipos de ingressos
class VIP(Ingresso): #VIP
    def __init__(self, valor, localizacao, adicional):
        super().__init__(valor, localizacao)
        self.adicional = adicional

    def getValor(self):
        return self.valor + self.adicional

class Normal(Ingresso): #ingreso normal
    def imprimeTipo(self):
        print("Ingresso Normal")

class CamaroteInferior(VIP): #camarote inferior
    def __init__(self, valor, localizacao, adicional):
        super().__init__(valor, localizacao, adicional)

class CamaroteSuperior(VIP): #camarote superior
    def __init__(self, valor, localizacao, adicional, adicionalSuperior):
        super().__init__(valor, localizacao, adicional)
        self.adicionalSuperior = adicionalSuperior

    def getValor(self):
        return self.valor + self.adicional + self.adicionalSuperior

def main():
    valor_base = 125.00  # valor padrao
    adicional_vip = 50.00  # valor adicional para se tornar VIP
    adicional_camarote_superior = 80.00  # valor adicional para se tornar do camarote superior

    localizacao = "area geral"

    print("Show do Manoel Gomes / caneta Azul: Digite 1 para Ingresso Normal | ou | 2 para Ingresso VIP:")
    tipo_ingresso = int(input())

    if tipo_ingresso == 1:
        ingresso = Normal(valor_base, localizacao)
        ingresso.imprimeTipo()
        ingresso.imprimeValor()
        ingresso.imprimeLocalizacao()
    elif tipo_ingresso == 2:
        print("Digite 1 para Camarote Superior | ou | 2 para Camarote Inferior:")
        tipo_camarote = int(input())

        if tipo_camarote == 1:
            localizacao = "Camarote Superior"
            ingresso = CamaroteSuperior(valor_base, localizacao, adicional_vip, adicional_camarote_superior)
            print("Ingresso VIP - Camarote Superior")
            ingresso.imprimeValor()
            ingresso.imprimeLocalizacao()
            print(f"Valor total: R$ {ingresso.getValor():.2f}")
        elif tipo_camarote == 2:
            localizacao = "Camarote Inferior"
            ingresso = CamaroteInferior(valor_base, localizacao, adicional_vip)
            print("Ingresso VIP - Camarote Inferior")
            ingresso.imprimeValor()
            ingresso.imprimeLocalizacao()
            print(f"Valor total: R$ {ingresso.getValor():.2f}")
    else:
        print("Opção invalida?")

if __name__ == "__main__": 
    main()



