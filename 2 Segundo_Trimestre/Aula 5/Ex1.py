class Pessoa:
    def __init__(self, nome, mae=None, pai=None):
        self.nome = nome
        self.mae = mae
        self.pai = pai

    # Verifica se duas pessoas possuem o mesmo nome e a mesma mãe
    def igualdade_semantica(self, outra_pessoa):
        return self.nome == outra_pessoa.nome and self.mae == outra_pessoa.mae

    # Verifica se duas pessoas são irmãs (mesma mãe ou pai)
    def sao_irmas(self, outra_pessoa):
        return self.mae == outra_pessoa.mae or self.pai == outra_pessoa.pai

    # Verifica se uma pessoa é antecessora (pai, mãe, avó, avô)
    def eh_antecessora(self, outra_pessoa):
        if self == outra_pessoa.mae or self == outra_pessoa.pai:
            return True
        if self == outra_pessoa.mae.mae or self == outra_pessoa.mae.pai or \
           self == outra_pessoa.pai.mae or self == outra_pessoa.pai.pai:
            return True
        return False


# Exemplo de uso
pessoa1 = Pessoa("Maria", mae="Ana")
pessoa2 = Pessoa("João", mae="Ana")
pessoa3 = Pessoa("Lucas", mae="Carla")

print(pessoa1.igualdade_semantica(pessoa2))  # False, pois os nomes são diferentes
print(pessoa1.sao_irmas(pessoa2))            # True, pois têm a mesma mãe
print(pessoa3.eh_antecessora(pessoa1))       # False, não é antecessora
