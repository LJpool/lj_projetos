class Pessoa:
    def __init__(self, nome, mae=None, pai=None):
        self.nome = nome
        self.mae = mae  # mae deve ser uma instância de Pessoa ou None
        self.pai = pai  # pai deve ser uma instância de Pessoa ou None

    # a) Método para verificar a igualdade semântica (mesmo nome e mesma mãe)
    def igualdade_semantica(self, outra_pessoa):
        return self.nome == outra_pessoa.nome and self.mae == outra_pessoa.mae

    # b) Método para verificar se duas pessoas são irmãs (mesma mãe ou mesmo pai)
    def sao_irmas(self, outra_pessoa):
        return self.mae == outra_pessoa.mae or self.pai == outra_pessoa.pai

    # c) Método para verificar se uma pessoa é antecessora (pai, mãe ou antecessores deles)
    def eh_antecessora(self, outra_pessoa):
        if self == outra_pessoa.mae or self == outra_pessoa.pai:
            return True
        if outra_pessoa.mae and self.eh_antecessora(outra_pessoa.mae):
            return True
        if outra_pessoa.pai and self.eh_antecessora(outra_pessoa.pai):
            return True
        return False

# Criando pessoas para teste
mae = Pessoa("Maria")
pai = Pessoa("João")
pessoa1 = Pessoa("Alice", mae=mae, pai=pai)
pessoa2 = Pessoa("Alice", mae=mae)  # Mesmo nome e mesma mãe
pessoa3 = Pessoa("Carlos", mae=mae, pai=pai)  # Irmão de pessoa1

# Teste de igualdade semântica
print(pessoa1.igualdade_semantica(pessoa2))  # True (mesmo nome e mãe)

# Teste se são irmãs
print(pessoa1.sao_irmas(pessoa3))  # True (mesma mãe e pai)

# Teste se pessoa1 é antecessora de pessoa3
print(mae.eh_antecessora(pessoa3))  # True (Maria é a mãe de Carlos)
print(pai.eh_antecessora(pessoa1))  # True (João é o pai de Alice)
