<<<<<<< HEAD
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
Explicação:
Classe: class Pessoa define uma nova classe chamada "Pessoa".
Método __init__: Função especial que roda quando um novo objeto da classe é criado. Aqui, a gente define os atributos como nome e idade.
self: Referência ao próprio objeto (é obrigatório nos métodos de classe).
Objeto: pessoa1 = Pessoa("João", 25) cria uma pessoa com nome "João" e idade 25.
Método: pessoa1.apresentar() faz a pessoa dizer seu nome e idade.
Isso é o básico! A POO em Python permite organizar o código de uma forma que fica mais fácil de trabalhar com objetos complexos.
'''
=======
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
Explicação:
Classe: class Pessoa define uma nova classe chamada "Pessoa".
Método __init__: Função especial que roda quando um novo objeto da classe é criado. Aqui, a gente define os atributos como nome e idade.
self: Referência ao próprio objeto (é obrigatório nos métodos de classe).
Objeto: pessoa1 = Pessoa("João", 25) cria uma pessoa com nome "João" e idade 25.
Método: pessoa1.apresentar() faz a pessoa dizer seu nome e idade.
Isso é o básico! A POO em Python permite organizar o código de uma forma que fica mais fácil de trabalhar com objetos complexos.
>>>>>>> a0834fef12c5679bb76b9d6580cf6e38308fd153
