import json

class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.codigo} - {self.nome}: R$ {self.preco:.2f}"

class Quarto:
    def __init__(self, numero, categoria, diaria):
        self.numero = numero
        self.categoria = categoria
        self.diaria = diaria
        self.consumo = []

    def adicionaConsumo(self, produto_codigo):
        self.consumo.append(produto_codigo)

    def totalConsumo(self, produtos):
        return sum(prod.preco for prod in produtos if prod.codigo in self.consumo)

    def limpaConsumo(self):
        self.consumo = []

    def __str__(self):
        return f"Quarto {self.numero} - Categoria {self.categoria} - Diária: R$ {self.diaria:.2f}"

class Reserva:
    def __init__(self, inicio, fim, cliente, quarto):
        self.inicio = inicio
        self.fim = fim
        self.cliente = cliente
        self.quarto = quarto
        self.status = 'A'  # A=Ativa, I=Check-in, O=Check-out, C=Cancelada

    def __str__(self):
        return f"Reserva de {self.cliente} no Quarto {self.quarto.numero} de {self.inicio} a {self.fim} - Status: {self.status}"

class Pousada:
    def __init__(self, nome, contato):
        self.nome = nome
        self.contato = contato
        self.quartos = []
        self.reservas = []
        self.produtos = []

    def consultaDisponibilidade(self, data, quarto_numero):
        for reserva in self.reservas:
            if reserva.quarto.numero == quarto_numero and reserva.status == 'A' and reserva.inicio <= data <= reserva.fim:
                return False
        return True

    def realizarReserva(self, inicio, fim, cliente, quarto_numero):
        if all(self.consultaDisponibilidade(dia, quarto_numero) for dia in range(inicio, fim+1)):
            quarto = next((q for q in self.quartos if q.numero == quarto_numero), None)
            if quarto:
                self.reservas.append(Reserva(inicio, fim, cliente, quarto))
                print("Reserva realizada com sucesso!")
            else:
                print("Quarto não encontrado.")
        else:
            print("Quarto indisponível no período.")

    def cancelarReserva(self, cliente):
        reserva = next((r for r in self.reservas if r.cliente == cliente and r.status == 'A'), None)
        if reserva:
            reserva.status = 'C'
            print("Reserva cancelada.")
        else:
            print("Reserva não encontrada.")

    def checkIn(self, cliente):
        reserva = next((r for r in self.reservas if r.cliente == cliente and r.status == 'A'), None)
        if reserva:
            reserva.status = 'I'
            print(f"Check-in realizado para {cliente}.")
        else:
            print("Reserva não encontrada.")

    def checkOut(self, cliente):
        reserva = next((r for r in self.reservas if r.cliente == cliente and r.status == 'I'), None)
        if reserva:
            total_diarias = (reserva.fim - reserva.inicio + 1) * reserva.quarto.diaria
            total_consumo = reserva.quarto.totalConsumo(self.produtos)
            reserva.status = 'O'
            reserva.quarto.limpaConsumo()
            print(f"Check-out realizado. Total: R$ {total_diarias + total_consumo:.2f}")
        else:
            print("Check-in não encontrado.")

    def registrarConsumo(self, cliente, produto_codigo):
        reserva = next((r for r in self.reservas if r.cliente == cliente and r.status == 'I'), None)
        if reserva:
            reserva.quarto.adicionaConsumo(produto_codigo)
            print("Consumo registrado.")
        else:
            print("Check-in não encontrado.")

    def salvarDados(self):
        dados = {
            'quartos': [{'numero': q.numero, 'categoria': q.categoria, 'diaria': q.diaria} for q in self.quartos],
            'reservas': [{'inicio': r.inicio, 'fim': r.fim, 'cliente': r.cliente, 'quarto_numero': r.quarto.numero, 'status': r.status} for r in self.reservas],
            'produtos': [{'codigo': p.codigo, 'nome': p.nome, 'preco': p.preco} for p in self.produtos]
        }
        with open('dados_pousada.json', 'w') as arquivo:
            json.dump(dados, arquivo)
        print("Dados salvos com sucesso!")

    def carregarDados(self):
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

def main():
    pousada = Pousada("Pousada Simplificada", "1234-5678")
    pousada.carregarDados()
    
    pousada.quartos = [Quarto(1, 'S', 100), Quarto(2, 'M', 150)]
    pousada.produtos = [Produto(1, 'Água', 5), Produto(2, 'Refrigerante', 7)]

    while True:
        opcao = input("\n1-Disponibilidade 2-Reserva 3-Cancelar Reserva 4-Check-In 5-Check-Out 6-Consumo 7-Salvar 0-Sair: ")
        if opcao == '1':
            data = int(input("Data: "))
            quarto_numero = int(input("Quarto: "))
            disponivel = pousada.consultaDisponibilidade(data, quarto_numero)
            print(f"Quarto {'disponível' if disponivel else 'indisponível'}")
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
            pousada.salvarDados()
        elif opcao == '0':
            pousada.salvarDados()
            break

if __name__ == "__main__":
    main()
