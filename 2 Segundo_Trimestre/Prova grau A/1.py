class jogadorFutebol:
    def __init__(self, nome, posicao, data_nascimento, nacionalidade, altura, peso):
        self.nome = nome
        self.posicao = posicao
        self.data_nascimento = data_nascimento 
        self.nacionalidade = nacionalidade
        self.altura = altura
        self.peso = peso

    def get_nome(self): #get
        return self.nome 
    def get_posicao(self):
        return self.posicao 
    def get_data_nascimento(self):
        return self.data_nascimento 
    def get_nacionalidade(self):
        return self.nacionalidade 
    def get_altura(self):
        return self.altura   
    def get_peso(self):
        return self.peso

    def set_nome(self, nome): #set
        self.nome = nome   
    def set_posicao(self, posicao):
        self.posicao = posicao    
    def set_data_nascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento    
    def set_nacionalidade(self, nacionalidade):
        self.nacionalidade = nacionalidade   
    def set_altura(self, altura):
        self.altura = altura    
    def set_peso(self, peso):
        self.peso = peso
    
    def imprimir_dados(self): #terminal
        print(f"nome: {self.nome}")
        print(f"posiçao: {self.posicao}")
        print(f"data de nascimento: {self.get_data_nascimento()}")
        print(f"nacionalidade: {self.nacionalidade}")
        print(f"altura: {self.altura} m")
        print(f"peso: {self.peso} kg")

    def calcular_idade(self): #calcular idade
        dia_nasc, mes_nasc, ano_nasc = map(int, self.data_nascimento.split('/'))
        hoje = (1, 10, 2024)
        dia_atual, mes_atual, ano_atual = hoje

        idade = ano_atual - ano_nasc
        if (mes_atual, dia_atual) < (mes_nasc, dia_nasc):
            idade -= 1
        return idade

    def tempo_ate_aposentadoria(self): #calcular aposentadoria
        idade = self.calcular_idade()
        if self.posicao == 'defesa':
            aposentadoria = 40
        elif self.posicao == 'meio-campo':
            aposentadoria = 38
        else:  
            aposentadoria = 35      
        if idade < aposentadoria:
            return aposentadoria - idade
        else:
            return 0

jogador = jogadorFutebol("Dumingus Silva", "defesa", "08/11/2005", "Brasileiro", 1.85, 80) #informaçao sobre o jogador
jogador.imprimir_dados()
print(f"idade: {jogador.calcular_idade()} anos")
print(f"tempo até aposentadoria: {jogador.tempo_ate_aposentadoria()} anos")
