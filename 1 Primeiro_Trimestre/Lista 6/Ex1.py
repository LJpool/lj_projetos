import random
from functools import reduce
v = [random.randint(10, 90) for _ in range(10)]

#a
print("Vetor v:", v)

#b
if 50 in v:
    print("O valor 50 está presente no vetor.")
else:
    print("O valor 50 não está presente no vetor.")

#c
num_ocorrencias_50 = v.count(50)
print("Número de ocorrências do valor 50:", num_ocorrencias_50)

#d
media = sum(v) / len(v)
print("Média dos valores do vetor:", media)

#e
maior_valor = max(v)
menor_valor = min(v)
print("Maior valor do vetor:", maior_valor)
print("Menor valor do vetor:", menor_valor)

#f
soma = sum(v)
produto_acumulado = reduce((lambda x, y: x * y), v)
print("Soma dos valores do vetor:", soma)
print("Produto acumulado dos valores do vetor:", produto_acumulado)

#g
v_inverso = v[::-1]
print("Vetor em ordem inversa:", v_inverso)

#h
v_inverso_copia = v_inverso.copy()
print("Cópia do vetor em ordem inversa:", v_inverso_copia)

#i
vPares = [num for num in v if num % 2 == 0]
vImpares = [num for num in v if num % 2 != 0]

#imprimir
print("Vetor de Pares:", vPares)
print("Vetor de Ímpares:", vImpares)