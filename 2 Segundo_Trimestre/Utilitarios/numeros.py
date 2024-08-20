'''
`int` em Python é um tipo de dado que representa números inteiros, ou seja, sem casas decimais. Também é uma função usada para converter outros tipos de dados (como strings ou floats) em inteiros.

Exemplos:

- Como tipo de dado: `x = 10` (a variável `x` é um `int`).
- Como função: `int("5")` converte a string `"5"` em `5`.

'''
'''
O que isso é f"Valor {i+1}: " ?

Isso é uma *f-string* em Python, uma forma de formatar strings que permite inserir expressões Python dentro de chaves `{}`. 
O `f` antes da string indica que é uma *f-string*. 

No exemplo `f"Valor {i+1}: "`, o valor da expressão `i+1` será calculado e inserido na posição correspondente dentro da string.

Se `i = 2`, por exemplo, a *f-string* resultará em `"Valor 3: "`.
'''

'''
As {} dentro de uma f-string são usadas para incluir expressões ou variáveis que serão avaliadas e inseridas na string resultante. 
Elas marcam o lugar onde o valor da expressão será colocado.

Exemplo:
'''
nome = "Payton"
idade = 25
mensagem = f"Nome: {nome}, Idade: {idade}"
'''
Aqui, as {} são substituídas pelos valores das variáveis nome e idade, resultando em "Nome: Payton, Idade: 25".
'''

#ola 