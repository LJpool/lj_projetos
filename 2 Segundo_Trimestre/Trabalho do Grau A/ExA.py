import json # modelo para salva da dos do projeto

class Produto: # a classe para os produtos de comsumo 
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def __str__(self): # volta em string dos produtos
        return f"{self.codigo} - {self.nome}: R$ {self.preco:.2f}"

class Quarto: # a classe Quarto 
    def __init__(self, numero, categoria, diaria):
        self.numero = numero
        self.categoria = categoria
        self.diaria = diaria
        self.consumo = [] # volta pros produtos consumidos

    def adicionaConsumo(self, produto_codigo): # colocar o produto ao consumo do quarto
        self.consumo.append(produto_codigo)

    def totalConsumo(self, produtos): # calcula o valor total do consumo dos produtos
        return sum(prod.preco for prod in produtos if prod.codigo in self.consumo)

    def limpaConsumo(self): # limpa a lista de consumo do quarto
        self.consumo = []

    def __str__(self): # volta para a representação em string do quarto
        return f"Quarto {self.numero} - Categoria {self.categoria} - Diária: R$ {self.diaria:.2f}" 

class Reserva: # classe para reservas na pousada
    def __init__(self, inicio, fim, cliente, quarto):
        self.inicio = inicio
        self.fim = fim
        self.cliente = cliente
        self.quarto = quarto
        self.status = 'A'  # A = ativa, I = check-in, O = check-out, C = cancelada

    def __str__(self): # voltar em string da reservas
        return f"Reserva de {self.cliente} no Quarto {self.quarto.numero} de {self.inicio} a {self.fim} - Status: {self.status}"

class Pousada: # classe para gerenciar o sistema da pousada
    def __init__(self, nome, contato):
        self.nome = nome
        self.contato = contato
        self.quartos = []
        self.reservas = []
        self.produtos = []

    def consultaDisponibilidade(self, data, quarto_numero): # verificaçao do quarto disponivel em uma data específica
        for reserva in self.reservas:
            if reserva.quarto.numero == quarto_numero and reserva.status == 'A' and reserva.inicio <= data <= reserva.fim:
                return False
        return True

    def realizarReserva(self, inicio, fim, cliente, quarto_numero): # fazre uma reserva para cliente o período solicitado
        if all(self.consultaDisponibilidade(dia, quarto_numero) for dia in range(inicio, fim+1)):
            quarto = next((q for q in self.quartos if q.numero == quarto_numero), None)
            if quarto:
                self.reservas.append(Reserva(inicio, fim, cliente, quarto))
                print("Reserva realizada com sucesso ;)")
            else:
                print("Quarto não encontrado :( ")
        else:
            print("Quarto indisponível no período :( ")

    def cancelarReserva(self, cliente): # cancelar uma reserva de um cliente
        reserva = next((r for r in self.reservas if r.cliente == cliente and r.status == 'A'), None)
        if reserva:
            reserva.status = 'C'
            print("Reserva cancelada ;) ")
        else:
            print("Reserva não encontrada :( ")

    def checkIn(self, cliente): # fazer o check-in de um cliente 
        reserva = next((r for r in self.reservas if r.cliente == cliente and r.status == 'A'), None)
        if reserva:
            reserva.status = 'I'
            print(f"Check-in realizado para {cliente} ;D ")
        else:
            print("Reserva não encontrada =( ")

    def checkOut(self, cliente):   # fazer o check-out de um cliente e calcula o total a ser pago
        reserva = next((r for r in self.reservas if r.cliente == cliente and r.status == 'I'), None)
        if reserva:
            total_diarias = (reserva.fim - reserva.inicio + 1) * reserva.quarto.diaria
            total_consumo = reserva.quarto.totalConsumo(self.produtos)
            reserva.status = 'O'
            reserva.quarto.limpaConsumo()
            print(f"Check-out realizado. Total: R$ {total_diarias + total_consumo:.2f}, volte sempre ;) ")
        else:
            print("Check-in não encontrado =( ")

    def registrarConsumo(self, cliente, produto_codigo):  # registra um produto consumido por um cliente
        reserva = next((r for r in self.reservas if r.cliente == cliente and r.status == 'I'), None)
        if reserva:
            reserva.quarto.adicionaConsumo(produto_codigo)
            print("Consumo registrado :P ")
        else:
            print("Check-in não encontrado :? ")

    def salvarDados(self): # salva os dados em um arquivo JSON
        dados = {
            'quartos': [{'numero': q.numero, 'categoria': q.categoria, 'diaria': q.diaria} for q in self.quartos],
            'reservas': [{'inicio': r.inicio, 'fim': r.fim, 'cliente': r.cliente, 'quarto_numero': r.quarto.numero, 'status': r.status} for r in self.reservas],
            'produtos': [{'codigo': p.codigo, 'nome': p.nome, 'preco': p.preco} for p in self.produtos]
        }
        with open('dados_pousada.json', 'w') as arquivo:
            json.dump(dados, arquivo)
        print("Dados salvos com sucesso!")

    def carregarDados(self): # isso carrega os dados do JSON SE EXISTIREM
        try:
            with open('dados_pousada.json', 'r') as arquivo:
                dados = json.load(arquivo)
                self.quartos = [Quarto(q['numero'], q['categoria'], q['diaria']) for q in dados['quartos']]
                self.produtos = [Produto(p['codigo'], p['nome'], p['preco']) for p in dados['produtos']]
                for r in dados['reservas']:
                    quarto = next((q for q in self.quartos if q.numero == r['quarto_numero']), None)
                    if quarto:
                        self.reservas.append(Reserva(r['inicio'], r['fim'], r['cliente'], quarto))
                        self.reservas[-1].status = r['status']
            print("Dados carregados com sucesso!")
        except FileNotFoundError:
            print("Nenhum dado encontrado, começando do zero.")

def main():# valores de produtos e quartos
    pousada = Pousada("Pousada Simplificada", "1234-5678")
    pousada.carregarDados()
    pousada.quartos = [
        Quarto(1, 'S', 100), Quarto(2, '2', 100), # exemplo de quartos 
        Quarto(3, 'S', 100), Quarto(4, 'M', 150), Quarto(5, 'M', 150),  
        Quarto(6, 'M', 150), Quarto(7, 'S', 200), Quarto(8, 'M', 200)  
    ]
    pousada.produtos = [Produto(1, 'Água', 4), Produto(2, 'Refrigerante', 6)] # exemplo de produtos 

    while True:  # menu do sistema
        opcao = input("\n1-Disponibilidade 2-Reserva 3-Cancelar Reserva 4-Check-In 5-Check-Out 6-Consumo 7-Limpar Consumo 8-Salvar 9-Carregar 0-Sair: ")
        if opcao == '1':
            data = int(input("Data: "))
            quarto_numero = int(input("Quarto: "))
            disponivel = pousada.consultaDisponibilidade(data, quarto_numero)
            print(f"O quarto está {'disponível' if disponivel else 'indisponível'}")
        elif opcao == '2':
            inicio = int(input("Início: "))
            fim = int(input("Fim: "))
            cliente = input("Cliente: ")
            quarto_numero = int(input("Quarto: "))
            pousada.realizarReserva(inicio, fim, cliente, quarto_numero)
        elif opcao == '3':
            cliente = input("Cliente: ")
            pousada.cancelarReserva(cliente)
        elif opcao == '4':
            cliente = input("Cliente: ")
            pousada.checkIn(cliente)
        elif opcao == '5':
            cliente = input("Cliente: ")
            pousada.checkOut(cliente)
        elif opcao == '6':
            cliente = input("Cliente: ")
            produto_codigo = int(input("Código do produto: "))
            pousada.registrarConsumo(cliente, produto_codigo)
        elif opcao == '7':
            quarto_numero = int(input("Número do Quarto para limpar consumo: "))
            quarto = next((q for q in pousada.quartos if q.numero == quarto_numero), None)
            if quarto:
                quarto.limpaConsumo()
                print("Consumo do quarto limpo com sucesso!")
            else:
                print("Quarto não encontrado!")
        elif opcao == '8':
            pousada.salvarDados()
        elif opcao == '9':
            pousada.carregarDados()
        elif opcao == '0':
            pousada.salvarDados()
            break

if __name__ == "__main__": # inicia o programa chamando a função main()
    main()