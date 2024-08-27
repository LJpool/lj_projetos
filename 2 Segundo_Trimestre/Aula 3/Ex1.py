# Hotel, Quarto, Cliente e Reserva
'''
Um cliente chega em um hotel e pede um quarto que esteja disponivel.
O atendente mostra os quartos e precos disponiveies.
O cliente escolhe o quato em questão
O consierje solicita as informacoes do cliente para efetua a rezerva. 
Apos a estadia o cliente solicitara o checkout do quarto.
Novamente o consierje solicita as informaçoes ao cliente para procurar a reserva. 
Apos é finalizado o checkout com suceso.
'''
'''
classes:
EX:
clasname
+fild: type
+method(type): type

Pesoa
-id: int
-nome: string
+ gatNome(void): string
'''

class quarto:
    def __init__(self, numero, tipo, preco ):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
