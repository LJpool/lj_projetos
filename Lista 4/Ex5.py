num_alunos = int(input("Entre com o número de alunos: "))

media_geral = 0

for aluno in range(1, num_alunos + 1):
    nota_a = float(input("Nota do Grau A do aluno {}: ".format(aluno)))
    nota_b = float(input("Nota do Grau B do aluno {}: ".format(aluno)))

    media = (nota_a * 1/3) + (nota_b * 2/3)
    media_geral += media

    if media >= 6.0:
        print("Aluno {} APROVADO".format(aluno))
    else:
        nota_c = float(input("Nota do Grau C do aluno {}: ".format(aluno)))
        grau_substituir = input("Qual grau deseja substituir (A ou B)? ").upper()

        if grau_substituir == 'A':
            media = (nota_c * 1/3) + (nota_b * 2/3)
        elif grau_substituir == 'B':
            media = (nota_a * 1/3) + (nota_c * 2/3)

        if media >= 6.0:
            print("Aluno {} APROVADO após substituição".format(aluno))
        else:
            print("Aluno {} REPROVADO após substituição".format(aluno))

media_geral /= num_alunos
print("Média geral dos alunos:", media_geral)