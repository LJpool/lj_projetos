pergunta = 'Qual é o verdadeiro nome do super-herói Batman?'
alternativaA = 'Bruce Wayne'
alternativaB = 'Clark Kent'
alternativaC = 'Peter Parker'
alternativaD = 'Tony Stark'
alternativaE = 'Steve Rogers'

print(pergunta)
print('a) ', alternativaA)
print('b) ', alternativaB)
print('c) ', alternativaC)
print('d) ', alternativaD)
print('e) ', alternativaE)

resposta_usuario = input('Digite a letra correspondente à resposta correta: ').lower()

# Verificando a resposta do usuário e exibindo a resposta correta
resposta_correta = 'a'

if resposta_usuario == resposta_correta:
    print(f'Você respondeu alternativa {resposta_usuario}. Parabéns! A resposta está correta.')
else:
    print(f'Você respondeu alternativa {resposta_usuario}. A resposta correta é a alternativa {resposta_correta}.')
