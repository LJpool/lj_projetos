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
'''
class quarto:
    def __init__(self, numero, tipo, preco ):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
'''

# Definindo as classes do sistema de gerenciamento de hotel

# Definindo as classes do sistema de gerenciamento de hotel

# Definindo as classes do sistema de gerenciamento de hotel

class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.disponivel = True
    
    def reservar(self):
        if self.disponivel:
            self.disponivel = False
        else:
            raise Exception("Quarto já reservado")
    
    def liberar(self):
        self.disponivel = True
    
    def __str__(self):
        status = "Disponível" if self.disponivel else "Reservado"
        return f"Quarto {self.numero} ({self.tipo}): {status} - Preço: R${self.preco:.2f}"

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def mostrar_detalhes(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}"

class Reserva:
    def __init__(self, cliente, quarto, dias):
        self.cliente = cliente
        self.quarto = quarto
        self.dias = dias
        self.total = self.calcular_total()
    
    def calcular_total(self):
        return self.dias * self.quarto.preco
    
    def __str__(self):
        return f"Reserva de {self.cliente.nome} no {self.quarto.numero}, Total: R${self.total:.2f} para {self.dias} dias"

class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.quartos = []
    
    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)
    
    def listar_quartos_disponiveis(self):
        disponiveis = [quarto for quarto in self.quartos if quarto.disponivel]
        if not disponiveis:
            print("Não há quartos disponíveis no momento.")
        else:
            print("Quartos disponíveis:")
            for quarto in disponiveis:
                print(quarto)
    
    def realizar_reserva(self, cliente, numero_quarto, dias):
        for quarto in self.quartos:
            if quarto.numero == numero_quarto and quarto.disponivel:
                quarto.reservar()
                reserva = Reserva(cliente, quarto, dias)
                print(f"Reserva realizada com sucesso: {reserva}")
                return
        print(f"Quarto {numero_quarto} não está disponível ou não existe.")
    
    def realizar_checkout(self, numero_quarto):
        for quarto in self.quartos:
            if quarto.numero == numero_quarto and not quarto.disponivel:
                quarto.liberar()
                print(f"Checkout realizado com sucesso. O {quarto} está disponível novamente.")
                return
        print(f"Quarto {numero_quarto} não está ocupado no momento.")

# Simulação interativa
if __name__ == "__main__":
    # Criando o hotel e os quartos
    hotel = Hotel("Hotel Central")
    hotel.adicionar_quarto(Quarto(30, "normal", 100.0))
    hotel.adicionar_quarto(Quarto(69, "luxo", 200.0))
    
    while True:
        print("\n1. Listar quartos disponíveis")
        print("2. Realizar reserva")
        print("3. Realizar checkout")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            hotel.listar_quartos_disponiveis()
        
        elif escolha == "2":
            nome_cliente = input("Digite o nome do cliente: ")
            cpf_cliente = input("Digite o CPF do cliente: ")
            cliente = Cliente(nome_cliente, cpf_cliente)
            
            hotel.listar_quartos_disponiveis()
            numero_quarto = int(input("Digite o número do quarto que deseja reservar: "))
            dias = int(input("Digite o número de dias de estadia: "))
            
            hotel.realizar_reserva(cliente, numero_quarto, dias)
        
        elif escolha == "3":
            numero_quarto = int(input("Digite o número do quarto para realizar o checkout: "))
            hotel.realizar_checkout(numero_quarto)
        
        elif escolha == "4":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

