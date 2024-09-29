# Definição da classe Pais
class Pais:
    def __init__(self, codigo_iso, nome, dimensao, populacao=0):
        self.codigo_iso = codigo_iso
        self.nome = nome
        self.dimensao = dimensao  # Em Km²
        self.populacao = populacao  # População inicial
        self.fronteiras = []  # Lista de países com os quais faz fronteira (máx. 40)

    # Métodos de acesso (getters e setters)
    def get_codigo_iso(self):
        return self.codigo_iso

    def set_codigo_iso(self, codigo_iso):
        self.codigo_iso = codigo_iso

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_populacao(self):
        return self.populacao

    def set_populacao(self, populacao):
        self.populacao = populacao

    def get_dimensao(self):
        return self.dimensao

    def set_dimensao(self, dimensao):
        self.dimensao = dimensao

    # Verificar igualdade semântica (mesmo código ISO)
    def igualdade_semantica(self, outro_pais):
        return self.codigo_iso == outro_pais.codigo_iso

    # Verificar se outro país é limítrofe (está na lista de fronteiras)
    def eh_limitrofe(self, outro_pais):
        return outro_pais in self.fronteiras

    # Retornar a densidade populacional (população / dimensão)
    def densidade_populacional(self):
        if self.dimensao > 0:
            return self.populacao / self.dimensao
        return 0

    # Retornar lista de vizinhos comuns entre dois países
    def vizinhos_comuns(self, outro_pais):
        return [pais for pais in self.fronteiras if pais in outro_pais.fronteiras]

    # Adicionar um país à lista de fronteiras
    def adicionar_fronteira(self, outro_pais):
        if len(self.fronteiras) < 40 and outro_pais not in self.fronteiras:
            self.fronteiras.append(outro_pais)
            outro_pais.adicionar_fronteira(self)  # Também adicionar o país como vizinho do outro país


# Definição da classe Continente
class Continente:
    def __init__(self, nome):
        self.nome = nome
        self.paises = []  # Lista de países que compõem o continente

    # Método para adicionar países ao continente
    def adicionar_pais(self, pais):
        self.paises.append(pais)

    # Método que retorne a dimensão total do continente
    def dimensao_total(self):
        return sum(pais.get_dimensao() for pais in self.paises)

    # Método que retorne a população total do continente
    def populacao_total(self):
        return sum(pais.get_populacao() for pais in self.paises)

    # Método que retorne a densidade populacional do continente
    def densidade_populacional(self):
        dimensao = self.dimensao_total()
        if dimensao > 0:
            return self.populacao_total() / dimensao
        return 0

    # Método que retorne o país com maior população no continente
    def pais_maior_populacao(self):
        if self.paises:
            return max(self.paises, key=lambda pais: pais.get_populacao())
        return None

    # Método que retorne o país com menor população no continente
    def pais_menor_populacao(self):
        if self.paises:
            return min(self.paises, key=lambda pais: pais.get_populacao())
        return None

    # Método que retorne o país de maior dimensão territorial no continente
    def pais_maior_dimensao(self):
        if self.paises:
            return max(self.paises, key=lambda pais: pais.get_dimensao())
        return None

    # Método que retorne o país de menor dimensão territorial no continente
    def pais_menor_dimensao(self):
        if self.paises:
            return min(self.paises, key=lambda pais: pais.get_dimensao())
        return None

    # Método que retorne a razão territorial do maior país em relação ao menor país
    def razao_territorial(self):
        maior = self.pais_maior_dimensao()
        menor = self.pais_menor_dimensao()
        if maior and menor and menor.get_dimensao() > 0:
            return maior.get_dimensao() / menor.get_dimensao()
        return 0


# Exemplo de uso
brasil = Pais("BRA", "Brasil", 8515767.049, 211000000)
argentina = Pais("ARG", "Argentina", 2780400, 45000000)
uruguai = Pais("URY", "Uruguai", 176215, 3500000)

# Criando o continente América do Sul
america_do_sul = Continente("América do Sul")
america_do_sul.adicionar_pais(brasil)
america_do_sul.adicionar_pais(argentina)
america_do_sul.adicionar_pais(uruguai)

# c) Dimensão total do continente
print(f"Dimensão total: {america_do_sul.dimensao_total()} km²")

# d) População total do continente
print(f"População total: {america_do_sul.populacao_total()} habitantes")

# e) Densidade populacional do continente
print(f"Densidade populacional: {america_do_sul.densidade_populacional()} hab/km²")

# f) País com maior população
print(f"País com maior população: {america_do_sul.pais_maior_populacao().get_nome()}")

# g) País com menor população
print(f"País com menor população: {america_do_sul.pais_menor_populacao().get_nome()}")

# h) País com maior dimensão territorial
print(f"País com maior dimensão: {america_do_sul.pais_maior_dimensao().get_nome()}")

# i) País com menor dimensão territorial
print(f"País com menor dimensão: {america_do_sul.pais_menor_dimensao().get_nome()}")

# j) Razão territorial do maior país em relação ao menor país
print(f"Razão territorial (maior/menor): {america_do_sul.razao_territorial()}")
