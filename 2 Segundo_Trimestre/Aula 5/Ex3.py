class Continente:
    def __init__(self, nome):
        self.nome = nome
        self.paises = []

    # Adiciona um país ao continente
    def adicionar_pais(self, pais):
        if len(self.paises) < 40:
            self.paises.append(pais)

    # Calcula a dimensão total do continente
    def dimensao_total(self):
        return sum(pais.get_dimensao_km2() for pais in self.paises)

    # Calcula a população total do continente
    def populacao_total(self):
        return sum(pais.get_populacao() for pais in self.paises if pais.get_populacao())

    # Calcula a densidade populacional do continente
    def densidade_populacional(self):
        pop_total = self.populacao_total()
        dim_total = self.dimensao_total()
        return pop_total / dim_total if dim_total else 0

    # Retorna o país com maior população
    def pais_com_maior_populacao(self):
        return max(self.paises, key=lambda pais: pais.get_populacao(), default=None)

    # Retorna o país com menor população
    def pais_com_menor_populacao(self):
        return min(self.paises, key=lambda pais: pais.get_populacao(), default=None)

    # Retorna o país com maior dimensão territorial
    def pais_com_maior_dimensao(self):
        return max(self.paises, key=lambda pais: pais.get_dimensao_km2(), default=None)

    # Retorna o país com menor dimensão territorial
    def pais_com_menor_dimensao(self):
        return min(self.paises, key=lambda pais: pais.get_dimensao_km2(), default=None)

    # Calcula a razão territorial entre o maior e o menor país
    def razao_territorial(self):
        maior = self.pais_com_maior_dimensao()
        menor = self.pais_com_menor_dimensao()
        if maior and menor:
            return maior.get_dimensao_km2() / menor.get_dimensao_km2()
        return 0


# Exemplo de uso
america_do_sul = Continente("América do Sul")

brasil = Pais("BRA", "Brasil", 8515767)
brasil.set_populacao(213000000)

argentina = Pais("ARG", "Argentina", 2780400)
argentina.set_populacao(45195777)

america_do_sul.adicionar_pais(brasil)
america_do_sul.adicionar_pais(argentina)

print(america_do_sul.dimensao_total())              # Soma da dimensão total
print(america_do_sul.populacao_total())             # Soma da população total
print(america_do_sul.densidade_populacional())      # Densidade populacional
print(america_do_sul.pais_com_maior_populacao().nome)  # País com maior população
print(america_do_sul.razao_territorial())           # Razão entre maior e menor país em dimensão

