#5. (3.0) Faça um programa que simule uma máquina de café e permita, através de um menu
#principal, executar as funções descritas nos itens (a, b, c e d) abaixo, e só termine quando o
#usuário escolhe a função desligar (d). A máquina prepara 3 opções de café: preto, com leite
#e cappuccino. Dentro dela, ela possui 4 compartimentos que armazenam até 1kg/1l dos
#ingredientes: café, água, leite e mistura para cappuccino. Cada compartimento recebe um
#refil de 1kg (sólidos) ou 1l (líquidos) dos ingredientes, e a máquina possui medidores
#eletrônicos que estimam a quantidade existente de cada um deles. Portanto, a qualquer
#momento, ela pode mostrar quanto ainda resta de cada um deles. As ações que podem ser
#feitas com a máquina são:

#a) Trocar o refil, indicando como parâmetro qual o tipo de ingrediente que deve ter o compartimento preenchido. 
#Após fazer a troca, o compartimento fica com a quantidade máxima do produto.

#b) Consultar a quantidade de um ingrediente. Para isso, é necessário informar como
#parâmetro o tipo do ingrediente e a máquina retorna no visor a quantidade dele.

#c) Preparar café, recebendo como parâmetro o tipo do café (preto, com leite ou
#cappuccino) e o dinheiro (os cafés custam R$1,00, R$1,50 e R$2,00,
#respectivamente) e retornando a bebida (em nosso programa, apenas uma
#mensagem na tela: CAFÉ PRONTO, RETIRE SUA BEBIDA!) e o troco correto do cliente.
#A compra é bem-sucedida (faz a bebida e retorna o troco, se necessário) se o dinheiro
#fornecido para a opção for maior ou igual ao preço do café e:

#i. Para a compra do café preto, houver 15g de café e 250ml de água na máquina.
#ii. Para a compra do café com leite, houver 20g de café e 250ml de leite na máquina
#iii. Para a compra do cappuccino, houver 40g de mistura de cappuccino e 300ml de água na máquina.
#iv. Caso não exista a quantidade suficiente de algum dos ingredientes do café a ser
#comprado, a máquina “devolve” o dinheiro do cliente e imprime o aviso:

#PRODUTO INDISPONÍVEL, DINHEIRO DEVOLVIDO.

#d) Desligar, que encerra o programa.
#OBS.: Assuma que a máquina sempre vai ter o troco correto, não estamos levando em
#conta a arrecadação.

########################################################################################################
class MaquinaCafe:
    def __init__(self):
        # Inicialização dos compartimentos da máquina com a quantidade máxima de cada ingrediente
        self.cafe = 1000  # 1000g de café
        self.agua = 1000  # 1000ml de água
        self.leite = 1000  # 1000ml de leite
        self.mistura_cappuccino = 1000  # 1000g de mistura para cappuccino

    def trocar_refil(self, ingrediente):
        # Método para trocar o refil de um ingrediente
        # O parâmetro ingrediente indica qual o tipo de ingrediente que deve ter o compartimento preenchido
        if ingrediente == "cafe":
            self.cafe = 1000  # Preenche o compartimento de café com a quantidade máxima
        elif ingrediente == "agua":
            self.agua = 1000  # Preenche o compartimento de água com a quantidade máxima
        elif ingrediente == "leite":
            self.leite = 1000  # Preenche o compartimento de leite com a quantidade máxima
        elif ingrediente == "cappuccino":
            self.mistura_cappuccino = 1000  # Preenche o compartimento de mistura para cappuccino com a quantidade máxima

    def consultar_quantidade(self, ingrediente):
        # Método para consultar a quantidade de um ingrediente na máquina
        # O parâmetro ingrediente indica qual o tipo do ingrediente a ser consultado
        if ingrediente == "cafe":
            return self.cafe  # Retorna a quantidade de café na máquina
        elif ingrediente == "agua":
            return self.agua  # Retorna a quantidade de água na máquina
        elif ingrediente == "leite":
            return self.leite  # Retorna a quantidade de leite na máquina
        elif ingrediente == "cappuccino":
            return self.mistura_cappuccino  # Retorna a quantidade de mistura para cappuccino na máquina

    def preparar_cafe(self, tipo_cafe, dinheiro):
        # Método para preparar café
        # Recebe como parâmetro o tipo de café a ser preparado e o valor em dinheiro inserido pelo usuário
        if tipo_cafe == "preto" and self.cafe >= 15 and self.agua >= 250:
            # Verifica se há ingredientes suficientes para preparar café preto
            self.cafe -= 15  # Deduz a quantidade de café utilizada
            self.agua -= 250  # Deduz a quantidade de água utilizada
            print("CAFÉ PRONTO, RETIRE SUA BEBIDA!")  # Mensagem indicando que o café está pronto
            return dinheiro - 1.00  # Retorna o troco correto para o cliente
        elif tipo_cafe == "com leite" and self.cafe >= 20 and self.leite >= 250:
            # Verifica se há ingredientes suficientes para preparar café com leite
            self.cafe -= 20  # Deduz a quantidade de café utilizada
            self.leite -= 250  # Deduz a quantidade de leite utilizada
            print("CAFÉ PRONTO, RETIRE SUA BEBIDA!")  # Mensagem indicando que o café está pronto
            return dinheiro - 1.50  # Retorna o troco correto para o cliente
        elif tipo_cafe == "cappuccino" and self.mistura_cappuccino >= 40 and self.agua >= 300:
            # Verifica se há ingredientes suficientes para preparar cappuccino
            self.mistura_cappuccino -= 40  # Deduz a quantidade de mistura para cappuccino utilizada
            self.agua -= 300  # Deduz a quantidade de água utilizada
            print("CAFÉ PRONTO, RETIRE SUA BEBIDA!")  # Mensagem indicando que o café está pronto
            return dinheiro - 2.00  # Retorna o troco correto para o cliente
        else:
            # Se não houver ingredientes suficientes para preparar o café desejado, devolve o dinheiro do cliente
            print("PRODUTO INDISPONÍVEL, DINHEIRO DEVOLVIDO.")
            return dinheiro

# Função principal para o menu
def menu():
    maquina = MaquinaCafe()  # Criação de uma instância da classe MaquinaCafe
    
    # Loop que exibe o menu principal e permite ao usuário interagir com a máquina até escolher a opção de desligar
    while True:
        print("\nMENU PRINCIPAL:")
        print("a) Trocar refil de ingrediente")
        print("b) Consultar quantidade de ingrediente")
        print("c) Preparar café")
        print("d) Desligar")

        opcao = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma opção do menu

        if opcao == "a":
            # Se o usuário escolher a opção "a", solicita qual ingrediente deseja trocar o refil
            ingrediente = input("Digite o ingrediente para trocar o refil: ")
            maquina.trocar_refil(ingrediente)  # Chama o método trocar_refil da classe MaquinaCafe
        elif opcao == "b":
            # Se o usuário escolher a opção "b", solicita qual ingrediente deseja consultar
            ingrediente = input("Digite o ingrediente para consultar a quantidade: ")
            # Chama o método consultar_quantidade da classe MaquinaCafe e exibe a quantidade do ingrediente
            print(f"Quantidade de {ingrediente}: {maquina.consultar_quantidade(ingrediente)}")
        elif opcao == "c":
            # Se o usuário escolher a opção "c", solicita o tipo de café a ser preparado e o valor em dinheiro
            tipo_cafe = input("Digite o tipo de café (preto, com leite, cappuccino): ")
            dinheiro = float(input("Digite o valor em dinheiro: "))
            # Chama o método preparar_cafe da classe MaquinaCafe para preparar o café e calcular o troco
            troco = maquina.preparar_cafe(tipo_cafe, dinheiro)
            print(f"Troco: R${troco:.2f}")  # Exibe o troco para o cliente
        elif opcao == "d":
            print("Máquina desligada.")  # Mensagem
########################################################################################################

# O WHILE  é uma estrutura de controle que cria um loop que executa um bloco de 
#código repetidamente enquanto uma condição específica for verdadeira.


#ELIF é uma abreviação de "else if" em Python. Ele é usado para adicionar uma condição alternativa após um if. 
#Se a condição do if não for verdadeira e a condição do elif for verdadeira, 
#o bloco de código associado ao elif será executado.

#DEF é uma palavra-chave em Python usada para definir uma função. 
#Ele cria um objeto de função e associa um nome a ele, 
#permitindo que você reutilize o bloco de código em diferentes partes do programa, 
#chamando a função pelo nome especificado.