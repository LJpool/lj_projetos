#usuario = matriz

usuario = [[0]*6 for _ in range(4)]
usuario[0] = [int(input(f"Valor {i + 1}: ")) for i in range(6)]
usuario[1] = usuario[0][::-1]
usuario[2] = [usuario[0][i] + usuario[1][i] for i in range(6)]

pares = [x for x in usuario[0] if x % 2 == 0]
impares = [x for x in usuario[0] if x % 2 != 0]
usuario[3] = pares + impares + [0] * (6 - len(pares) - len(impares))

print("\nMatriz 1:")
for linha in usuario:
    print("\t".join(map(str, linha)))

print("\nMatriz 2:")
for linha in zip(*usuario):
    print("\t".join(map(str, linha)))