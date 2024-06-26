v1 = [1, 5, 9, 2, 5]
v2 = [7, 4, 13, 21, 6]
v3 = [8, -3, 5, 7, 12]

M = [v1, v2, v3]

print("Matriz M original:")
for linha in M:
    print(' '.join(map(str, linha)))

for i in range(len(M)):
    for j in range(len(M[i])):
        M[i][j] *= 7

print("\nMatriz M após multiplicação por 7:")
for linha in M:
    print(' '.join(map(str, linha)))