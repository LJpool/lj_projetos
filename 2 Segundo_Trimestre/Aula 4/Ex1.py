class Pessoa:
    def __init__(self, nome, sexo, corOlhos, pai=None, mae=None):
        self.nome = nome
        self.sexo = sexo
        self.corOlhos = corOlhos
        self.pai = pai
        self.mae = mae
        # Validação inicial
        self.setSexo(sexo)
        self.setCorOlhos(corOlhos)

    def setSexo(self, sexo):
        if sexo in ['M', 'F']:
            self.sexo = sexo
        else:
            raise ValueError("Sexo inválido. Use 'M' para Masculino ou 'F' para Feminino.")

    def setCorOlhos(self, corOlhos):
        if corOlhos in ['C', 'V', 'A']:
            self.corOlhos = corOlhos
        else:
            raise ValueError("Cor de olhos inválida. Use 'C' para Castanho, 'V' para Verde ou 'A' para Azul.")

    def getNome(self):
        return self.nome

    def getSexoStr(self):
        return "Masculino" if self.sexo == 'M' else "Feminino"

    def getCorOlhosStr(self):
        cores = {'C': "Castanho", 'V': "Verde", 'A': "Azul"}
        return cores[self.corOlhos]

    def imprimeDados(self):
        print(f"Nome: {self.nome}")
        print(f"Sexo: {self.getSexoStr()}")
        print(f"Cor dos olhos: {self.getCorOlhosStr()}")
        print(f"Pai: {self.pai.nome if self.pai else 'Desconhecido'}")
        print(f"Mãe: {self.mae.nome if self.mae else 'Desconhecida'}")

    def geraPessoa(self, nome, sexo, pai):
        if self.sexo != 'F':
            print("Apenas pessoas do sexo feminino podem gerar outra pessoa.")
            return None
        if pai.sexo != 'M':
            print("O pai deve ser do sexo masculino.")
            return None
        
        # Determinação da cor dos olhos com base na dominância
        corOlhos = self.determinaCorOlhos(pai)
        return Pessoa(nome, sexo, corOlhos, pai, self)

    def determinaCorOlhos(self, pai):
        # Regras de dominância: C > V > A
        if 'C' in [self.corOlhos, pai.corOlhos]:
            return 'C'
        elif 'V' in [self.corOlhos, pai.corOlhos]:
            return 'V'
        else:
            return 'A'

# Função principal para demonstrar o uso da classe
def main():
    pai = Pessoa("Carlos", 'M', 'C')
    mae = Pessoa("Maria", 'F', 'V')
    filho = mae.geraPessoa("João", 'M', pai)
    
    if filho:
        filho.imprimeDados()

# Execução do código
main()
