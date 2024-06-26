import random

#array uzado
array = ['p', 'e', 't', 'e', 'r']
print("Array inicial:", array)

#tamanho do array
n = len(array)

#embaralhamento
for _ in range(n):
    i = random.randint(0, n-1)
    j = random.randint(0, n-1)
    array[i], array[j] = array[j], array[i]

print("Array embaralhado:", array)
