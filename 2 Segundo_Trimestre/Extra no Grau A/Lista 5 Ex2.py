class Pais:
    def __init__(self, codigo_iso, nome, dimensao, populacao=0):
        self.codigo_iso = codigo_iso
        self.nome = nome
        self.dimensao = dimensao  # Em Km²
        self.populacao = populacao  # População inicial
        self.fronteiras = []  # Lista de países com os quais faz fronteira (máx. 40)

    # b) Métodos de acesso (getters e setters)
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

    # c) Verificar igualdade semântica (mesmo código ISO)
    def igualdade_semantica(self, outro_pais):
        return self.codigo_iso == outro_pais.codigo_iso

    # d) Verificar se outro país é limítrofe (está na lista de fronteiras)
    def eh_limitrofe(self, outro_pais):
        return outro_pais in self.fronteiras

    # e) Retornar a densidade populacional (população / dimensão)
    def densidade_populacional(self):
        if self.dimensao > 0:
            return self.populacao / self.dimensao
        return 0

    # f) Retornar lista de vizinhos comuns entre dois países
    def vizinhos_comuns(self, outro_pais):
        return [pais for pais in self.fronteiras if pais in outro_pais.fronteiras]

    # Adicionar um país à lista de fronteiras
    def adicionar_fronteira(self, outro_pais):
        if len(self.fronteiras) < 40 and outro_pais not in self.fronteiras:
            self.fronteiras.append(outro_pais)
            outro_pais.adicionar_fronteira(self)  # Também adicionar o país como vizinho do outro país

# Exemplo de uso
brasil = Pais("BRA", "Brasil", 8515767.049, 211000000)
argentina = Pais("ARG", "Argentina", 2780400, 45000000)
uruguai = Pais("URY", "Uruguai", 176215, 3500000)

# Adicionando fronteiras
brasil.adicionar_fronteira(argentina)
brasil.adicionar_fronteira(uruguai)
argentina.adicionar_fronteira(uruguai)

# c) Teste de igualdade semântica
print(brasil.igualdade_semantica(argentina))  # False

# d) Verificar se são países limítrofes
print(brasil.eh_limitrofe(argentina))  # True

# e) Densidade populacional do Brasil
print(brasil.densidade_populacional())  # População / Dimensão = ~24,77 hab/km²

# f) Vizinhos comuns entre Brasil e Argentina
print([pais.nome for pais in brasil.vizinhos_comuns(argentina)])  # ['Uruguai']
