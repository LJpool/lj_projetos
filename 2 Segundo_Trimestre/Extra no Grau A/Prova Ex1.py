#todas as mudanças que coloquei estão com o jogo da velha.

from datetime import datetime

class JogadorFutebol:
    def __init__(self, nome, posicao, data_nascimento, nacionalidade, altura, peso):
        self._nome = nome
        self._posicao = posicao
        self._data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')  #usar datetime
        self._nacionalidade = nacionalidade
        self._altura = altura
        self._peso = peso

    #usando property para criar getter e setter
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def posicao(self):
        return self._posicao

    @posicao.setter
    def posicao(self, posicao):
        self._posicao = posicao

    @property
    def data_nascimento(self):
        return self._data_nascimento.strftime('%d/%m/%Y')  #convertendo para string na exibiçao

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self._data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')

    @property
    def nacionalidade(self):
        return self._nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        self._nacionalidade = nacionalidade

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    def imprimir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Posição: {self.posicao}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"Nacionalidade: {self.nacionalidade}")
        print(f"Altura: {self.altura} m")
        print(f"Peso: {self.peso} kg")

    def calcular_idade(self): 
        hoje = datetime.now()
        idade = hoje.year - self._data_nascimento.year
        if (hoje.month, hoje.day) < (self._data_nascimento.month, self._data_nascimento.day):
            idade -= 1
        return idade

    def tempo_ate_aposentadoria(self):
        idade = self.calcular_idade()
        if self.posicao == 'defesa':
            aposentadoria = 40
        elif self.posicao == 'meio-campo':
            aposentadoria = 38
        else:
            aposentadoria = 35
        return max(aposentadoria - idade, 0)  #garantir que o valor não seja negativo

# Teste
jogador = JogadorFutebol("Dumingus Silva", "defesa", "08/11/2005", "Brasileiro", 1.85, 80)
jogador.imprimir_dados()
print(f"Idade: {jogador.calcular_idade()} anos")
print(f"Tempo até aposentadoria: {jogador.tempo_ate_aposentadoria()} anos")
