#RETURN em Python encerra uma função e retorna um valor para onde a função foi chamada;
#Ele é usado para comunicar o resultado da função de volta ao código que a chamou.

#O RANGE em Python cria uma sequência de números usada em loops, definindo início, fim e passo. 
#Ele é útil para iterar sobre uma faixa específica de valores. No código da função e_primo, 
#o range é usado para verificar a divisibilidade do número em um intervalo limitado, 
#melhorando a eficiência do algoritmo.


# O WHILE  é uma estrutura de controle que cria um loop que executa um bloco de 
#código repetidamente enquanto uma condição específica for verdadeira.


#ELIF é uma abreviação de "else if" em Python. Ele é usado para adicionar uma condição alternativa após um if. 
#Se a condição do if não for verdadeira e a condição do elif for verdadeira, 
#o bloco de código associado ao elif será executado.

#DEF é uma palavra-chave em Python usada para definir uma função. 
#Ele cria um objeto de função e associa um nome a ele, 
#permitindo que você reutilize o bloco de código em diferentes partes do programa, 
#chamando a função pelo nome especificado.

#bastante usado
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
#for i in range(2, int(num**0.5) + 1):
#Essa parte do código significa que estamos iterando sobre todos os números de 2 até a raiz quadrada de num (arredondada para cima), 
#mais 1. Isso nos permite verificar se num é divisível por algum desses números e determinar se ele é primo.