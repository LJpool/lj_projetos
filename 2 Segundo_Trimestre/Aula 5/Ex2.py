class Pais:
    def __init__(self, codigo_iso, nome, dimensao_km2):
        self.codigo_iso = codigo_iso
        self.nome = nome
        self.populacao = None
        self.dimensao_km2 = dimensao_km2
        self.fronteiras = []

    # Getters e setters
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

    def get_dimensao_km2(self):
        return self.dimensao_km2

    def set_dimensao_km2(self, dimensao_km2):
        self.dimensao_km2 = dimensao_km2

    # Verifica se dois países são semanticamente iguais (mesmo código ISO)
    def igualdade_semantica(self, outro_pais):
        return self.codigo_iso == outro_pais.codigo_iso

    # Verifica se dois países são limitrofes (fazem fronteira)
    def eh_limitrofe(self, outro_pais):
        return outro_pais in self.fronteiras

    # Calcula a densidade populacional
    def densidade_populacional(self):
        return self.populacao / self.dimensao_km2 if self.populacao and self.dimensao_km2 else 0

    # Retorna vizinhos em comum entre dois países
    def vizinhos_comuns(self, outro_pais):
        return list(set(self.fronteiras) & set(outro_pais.fronteiras))


# Exemplo de uso
brasil = Pais("BRA", "Brasil", 8515767)
argentina = Pais("ARG", "Argentina", 2780400)

brasil.set_populacao(213000000)
argentina.set_populacao(45195777)

brasil.fronteiras = [argentina]
argentina.fronteiras = [brasil]

print(brasil.igualdade_semantica(argentina))  # False, países têm códigos ISO diferentes
print(brasil.eh_limitrofe(argentina))        # True, fazem fronteira
print(brasil.densidade_populacional())       # Calcula a densidade populacional do Brasil
print(brasil.vizinhos_comuns(argentina))     # Retorna os vizinhos em comum
