#erro desconhecido 
import csv

with open('benchmark.csv', newline='') as file:
    reader = csv.DictReader(file)
    dados = list(reader)
 
'''
for dado in dados:
    cpu = float(dado['cpu'])
    memoria = float(dado['memória'])
    tempo = float(dado['tempo'])
    linhas = int(dado['linhas'])
    dado['desempenho'] = 10**6 / (cpu * 100 + memoria + tempo + linhas)
'''