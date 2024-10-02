'''
rogramação orientada a objetos (POO) em Python é um jeito de organizar o código ao redor de "objetos", 
que representam coisas do mundo real. O jeito mais fácil de entender isso é com exemplos.

Passos básicos:
1. Criação de uma classe: Uma classe é como um molde ou modelo que define as características e ações de um objeto.
2. Atributos: São as características (dados) do objeto.
3. Métodos: São as ações (funções) que o objeto pode executar.
4. Instância: Quando você cria um objeto específico a partir de uma classe.
Vamos fazer isso na prática:

Exemplo básico de uma classe "Pessoa":
'''
'''
# Criando a classe
class Pessoa:
    # Método especial __init__ para definir os atributos da pessoa
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo nome
        self.idade = idade  # Atributo idade

    # Método para exibir informações da pessoa
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Criando um objeto a partir da classe Pessoa (instanciando)
pessoa1 = Pessoa("João", 25)

# Usando o método da classe
pessoa1.apresentar()
'''
'''
Explicação:
Classe: class Pessoa define uma nova classe chamada "Pessoa".
Método __init__: Função especial que roda quando um novo objeto da classe é criado. Aqui, a gente define os atributos como nome e idade.
self: Referência ao próprio objeto (é obrigatório nos métodos de classe).
Objeto: pessoa1 = Pessoa("João", 25) cria uma pessoa com nome "João" e idade 25.
Método: pessoa1.apresentar() faz a pessoa dizer seu nome e idade.
Isso é o básico! A POO em Python permite organizar o código de uma forma que fica mais fácil de trabalhar com objetos complexos.
'''

class jogadorFutebol:
    def __init__(self, nome, posicao, data_nascimento, nacionalidade, altura, peso):
        self.nome = nome
        self.posicao = posicao
        self.data_nascimento = data_nascimento 
        self.nacionalidade = nacionalidade
        self.altura = altura
        self.peso = peso

    def get_nome(self):
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

    def set_nome(self, nome):
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
    
    def imprimir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Posição: {self.posicao}")
        print(f"Data de Nascimento: {self.get_data_nascimento()}")
        print(f"Nacionalidade: {self.nacionalidade}")
        print(f"Altura: {self.altura} m")
        print(f"Peso: {self.peso} kg")

    def calcular_idade(self):
        dia_nasc, mes_nasc, ano_nasc = map(int, self.data_nascimento.split('/'))
        hoje = (1, 10, 2024)
        dia_atual, mes_atual, ano_atual = hoje

        idade = ano_atual - ano_nasc
        if (mes_atual, dia_atual) < (mes_nasc, dia_nasc):
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
        
        if idade < aposentadoria:
            return aposentadoria - idade
        else:
            return 0

jogador = jogadorFutebol("Dumingus Silva", "defesa", "08/11/2005", "Brasileiro", 1.85, 80)
jogador.imprimir_dados()
print(f"Idade: {jogador.calcular_idade()} anos")
print(f"Tempo até aposentadoria: {jogador.tempo_ate_aposentadoria()} anos")
