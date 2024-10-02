class data:
    def __init__(self, dia, mes, ano):
        if self.data_valida(dia, mes, ano):
            self.dia = dia
            self.mes = mes
            self.ano = ano
        else:
            self.dia = 1
            self.mes = 1
            self.ano = 1

    def data_valida(self, dia, mes, ano): #validar data
        if mes < 1 or mes > 12:
            return False
        if dia < 1 or dia > 31:
            return False
        if mes in [4, 6, 9, 11] and dia > 30:
            return False
        if mes == 2:
            if self.is_bissexto(ano):
                return dia <= 29
            else:
                return dia <= 28
        return True

    def compara(self, outra_data): #ver as duas datas
        if self.ano > outra_data.ano:
            return 1
        elif self.ano < outra_data.ano:
            return -1
        elif self.mes > outra_data.mes:
            return 1
        elif self.mes < outra_data.mes:
            return -1
        elif self.dia > outra_data.dia:
            return 1
        elif self.dia < outra_data.dia:
            return -1
        else:
            return 0


    def get_dia(self): #valtar dias
        return self.dia
    def get_mes(self): #voltar mes do dia exato
        return self.mes
    def get_mes_extenso(self): #meses
        meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
                 "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        return meses[self.mes - 1]
    def get_ano(self): #ano da data
        return self.ano
    def is_bissexto(self, ano=None): #ano bissexto
        if ano is None:
            ano = self.ano
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

data1 = data(1, 7, 2014) #sistema em si 
data2 = data(1, 10, 2024)

print("data 1:", data1.get_dia(), "/", data1.get_mes(), "/", data1.get_ano())
print("data 2:", data2.get_dia(), "/", data2.get_mes(), "/", data2.get_ano())

print("comparação entre datas:", data1.compara(data2)) 
print("mês da Data 1 por extenso:", data1.get_mes_extenso())
print("ano da Data 1 é bissexto?", data1.is_bissexto())
