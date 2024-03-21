nota_grau_a = float(input("Digite a nota do Grau A: "))
nota_grau_b = float(input("Digite a nota do Grau B: "))

media_final = (nota_grau_a * 1/3) + (nota_grau_b * 2/3)

if media_final >= 6.0:
    print("Média final:", media_final)
    print("O aluno foi aprovado.")
else:
    print("Média final:", media_final)
    opcao = input("O aluno ficou em recuperação. Deseja substituir o Grau A ou o Grau B (a/b)? ").lower()
    
    if opcao == 'a':
        nota_grau_a = float(input("Digite a nova nota do Grau A: "))
    elif opcao == 'b':
        nota_grau_b = float(input("Digite a nova nota do Grau B: "))
    else:
        print("Opção inválida!")

    media_final = (nota_grau_a * 1/3) + (nota_grau_b * 2/3)

    if media_final >= 6.0:
        print("Média final após substituição:", media_final)
        print("O aluno foi aprovado após substituição.")
    else:
        print("Média final após substituição:", media_final)
        print("O aluno foi reprovado após substituição.")
