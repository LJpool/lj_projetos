preco_produto = float(input("Digite o preço normal do produto: "))
condicao_pagamento = int(input("Escolha a condição de pagamento (1 - à vista em dinheiro, 2 - à vista no cartão de crédito, 3 - em duas vezes, 4 - em três vezes): "))

if condicao_pagamento == 1:
    valor_pago = preco_produto * 0.85  
elif condicao_pagamento == 2:
    valor_pago = preco_produto * 0.90  
elif condicao_pagamento == 3:
    valor_pago = preco_produto  
elif condicao_pagamento == 4:
    valor_pago = preco_produto * 1.10  
else:
    valor_pago = preco_produto 

print("O valor a ser pago pelo produto é R$", valor_pago)