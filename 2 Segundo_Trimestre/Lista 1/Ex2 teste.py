'''
import csv

with open('benchmark.csv', newline='') as file:
    reader = csv.DictReader(file)
    dados = list(reader)

    

for dado in dados:
    cpu = float(dado['cpu'])
    memoria = float(dado['memória'])
    tempo = float(dado['tempo'])
    linhas = int(dado['linhas'])
    dado['desempenho'] = 10**6 / (cpu * 100 + memoria + tempo + linhas)
'''

import csv

# Função para calcular o desempenho
def calcular_desempenho(cpu, memoria, tempo, linhas):
    return 106 / (cpu * 100 + memoria + tempo + linhas)

# Inicializar variáveis
dados = []
desempenhos = []
somas = {'cpu': 0, 'memoria': 0, 'tempo': 0, 'linhas': 0, 'desempenho': 0}

# Ler o arquivo CSV
try:
    with open('dados_benchmark.csv', newline='') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            cpu = float(linha['cpu'])
            memoria = float(linha['memória'])
            tempo = float(linha['tempo'])
            linhas = int(linha['linhas'])
            desempenho = calcular_desempenho(cpu, memoria, tempo, linhas)
            
            dados.append({
                'linguagem': linha['linguagem'],
                'cpu': cpu,
                'memória': memoria,
                'tempo': tempo,
                'linhas': linhas,
                'desempenho': desempenho
            })
            
            # Acumular valores para cálculo da média
            somas['cpu'] += cpu
            somas['memoria'] += memoria
            somas['tempo'] += tempo
            somas['linhas'] += linhas
            somas['desempenho'] += desempenho
            
            desempenhos.append(desempenho)
            
except FileNotFoundError:
    print("Erro: O arquivo 'dados_benchmark.csv' não foi encontrado.")
    exit()
except Exception as e:
    print(f"Erro ao ler o arquivo CSV: {e}")
    exit()

# a) Listagem dos desempenhos
print("Desempenho por linguagem:")
for dado in dados:
    print(f"Linguagem: {dado['linguagem']}, Desempenho: {dado['desempenho']:.2f}")

# b) Média das métricas
n = len(dados)
média_métricas = {
    'cpu': somas['cpu'] / n,
    'memória': somas['memoria'] / n,
    'tempo': somas['tempo'] / n,
    'linhas': somas['linhas'] / n,
    'desempenho': somas['desempenho'] / n
}

print("\nMédia das métricas:")
for métrica, valor in média_métricas.items():
    print(f"{métrica}: {valor:.3f}")

# c) Linguagem com maior desempenho
linguagem_maior_desempenho = max(dados, key=lambda x: x['desempenho'])['linguagem']
print(f"\nLinguagem com maior desempenho: {linguagem_maior_desempenho}")

# d) Linguagem com menor número de linhas
linguagem_menor_linhas = min(dados, key=lambda x: x['linhas'])['linguagem']
print(f"Linguagem com menor número de linhas: {linguagem_menor_linhas}")

