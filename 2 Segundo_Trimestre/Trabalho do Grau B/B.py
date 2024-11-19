import pickle  #modelo para salva da dos do projeto
import os

############## classe Process e subclasses ##########
class Process: # classe base para o Process
    def __init__(self, pid): # inicializa o processo com PID unico 
        self.pid = pid

    def execute(self):
        pass  # metodo execute que sera implementado nas subclasses adiante

class ComputingProcess(Process): # subclasse para processo dos calculos
    def __init__(self, pid, expression):
        super().__init__(pid)
        self.expression = expression # armazena as expreçoes para calculo

    def execute(self):
        operands = self.expression.split() # vai divide expressao em operandos e operador
        if len(operands) == 3:
            op1, operator, op2 = operands
            try:
                op1, op2 = float(op1), float(op2) # converte operandos em numeros
                if operator == '+':  # vai realiza o calculo com base no operador pedido
                    result = op1 + op2
                elif operator == '-':
                    result = op1 - op2
                elif operator == '*':
                    result = op1 * op2
                elif operator == '/':
                    result = op1 / op2
                else:
                    print("operador desconhecido")
                    return
                print(f"resultado da expressão {self.expression}: {result}")
            except ValueError:
                print("Erro: operandos invalidos")
        else:
            print("Expressão malfeita")

class WritingProcess(Process): # a subclasse para processos de gravaçao 
    def __init__(self, pid, expression):
        super().__init__(pid)
        self.expression = expression # expresao a ser gravada

    def execute(self):
        with open("computation.txt", "a") as file: # vai abrir o arquivo e grava a expressão nele
            file.write(self.expression + "\n")
        print(f"Expressão '{self.expression}' gravada no arquivo.")

class ReadingProcess(Process): # subclasse pro processo de leitura
    def __init__(self, pid, process_list):
        super().__init__(pid)
        self.process_list = process_list # faz referencia pra lista de processos

    def execute(self):
        try:
            with open("computation.txt", "r") as file:  # vsi sbrir o arquivo e le as linhas
                lines = file.readlines()
                for line in lines:
                    expression = line.strip()
                    if expression:
                        new_pid = len(self.process_list) + 1 # vai cria novos processos de calculo e adiciona na lista
                        self.process_list.append(ComputingProcess(new_pid, expression))
            open("computation.txt", "w").close()  # limpa de arquivo apos a leitura
            print("Arquivo lido e processos de cálculo criados")
        except FileNotFoundError:
            print("Arquivo computation.txt não encontrado")

class PrintingProcess(Process): # subclasse para processos de impressão
    def __init__(self, pid, process_list):
        super().__init__(pid)
        self.process_list = process_list # referencia lista de processos

    def execute(self):
        print("Fila de processos:") # vai imprimir os detalhes da fila de processos
        for process in self.process_list:
            print(f"PID: {process.pid}, Tipo: {type(process).__name__}")

######### funçoes do sistema de processos ###########

process_list = [] # lista de processos

def create_process(): # as funçoes de gerenciamento de processos
    print("\nSelecione o tipo de processo para criar:")
    print("1 - ComputingProcess | Processo de Cálculo")
    print("2 - WritingProcess | Processo de Gravação")
    print("3 - ReadingProcess | Processo de Leitura")
    print("4 - PrintingProcess | Processo de Impressão")

    choice = input("Digite o número correspondente ao tipo de processo: ")
    pid = len(process_list) + 1 # vai gerar o prpximo PID

    if choice == "1":
        expression = input("Digite a expressão ex: 2 + 2 : ") # cria um processo de cálculo
        process = ComputingProcess(pid, expression)
        process_list.append(process)
        print(f"Processo de Cálculo criado com PID {pid}.")
    elif choice == "2":
        expression = input("Digite a expressão para gravar ex: 2 * 2 : ") # cria um processo de gravaçao
        process = WritingProcess(pid, expression)
        process_list.append(process)
        print(f"Processo de Gravação criado com PID {pid}.")
    elif choice == "3":
        process = ReadingProcess(pid, process_list) # cria um processo de leitura
        process_list.append(process)
        print(f"Processo de Leitura criado com PID {pid}.")
    elif choice == "4":
        process = PrintingProcess(pid, process_list)
        process_list.append(process)
        print(f"Processo de Impressão criado com PID {pid}.") # cria um processo de impressão
    else:
        print("Opção inválida?")

def execute_next_process():
    if not process_list: # vai executa o proximo processo na fila
        print("A fila de processos está vazia.")
        return
    next_process = process_list.pop(0)
    print(f"\nExecutando o processo com PID {next_process.pid}...")
    next_process.execute() # executa o processo

def execute_specific_process():
    if not process_list: # executa algum processo específico com o PID ja gerado 
        print("A fila de processos está vazia.")
        return

    try:
        pid = int(input("Digite o PID do processo que deseja executar: "))
    except ValueError:
        print("PID inválido.")
        return

    for process in process_list:
        if process.pid == pid:
            process_list.remove(process) # remove o processo da fila
            print(f"\nExecutando o processo com PID {pid}...")
            process.execute()
            return

    print(f"Nenhum processo com PID {pid} foi encontrado.")

def save_process_list(): # salva a lista um arquivo
    try:
        with open("process_list.txt", "w") as file:
            for process in process_list:
                if isinstance(process, ComputingProcess):
                    file.write(f"ComputingProcess,{process.pid},{process.expression}\n")
                elif isinstance(process, WritingProcess):
                    file.write(f"WritingProcess,{process.pid},{process.expression}\n")
                elif isinstance(process, ReadingProcess):
                    file.write(f"ReadingProcess,{process.pid}\n")
                elif isinstance(process, PrintingProcess):
                    file.write(f"PrintingProcess,{process.pid}\n")
        print("Fila de processos salva com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar a fila de processos: {e}")

def load_process_list(): # carrega a lista de processos de um arquivo
    try: 
        with open("process_list.txt", "r") as file:
            process_list.clear() # limpa a lista atual
            for line in file:
                data = line.strip().split(",")
                process_type, pid = data[0], int(data[1])
                if process_type == "ComputingProcess":
                    expression = data[2]
                    process_list.append(ComputingProcess(pid, expression))
                elif process_type == "WritingProcess":
                    expression = data[2]
                    process_list.append(WritingProcess(pid, expression))
                elif process_type == "ReadingProcess":
                    process_list.append(ReadingProcess(pid, process_list))
                elif process_type == "PrintingProcess":
                    process_list.append(PrintingProcess(pid, process_list))
        print("Fila de processos carregada com sucesso.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar a fila de processos: {e}")

############## Menu Principal ##############

while True:
    print("\n--- Menu ---")
    print("1 - Criar processo")
    print("2 - Executar próximo processo")
    print("3 - Executar processo específico")
    print("4 - Salvar a fila de processos")
    print("5 - Carregar a fila de processos")
    print("0 - Sair")
    option = input("Escolha uma opção: ")

    if option == "1":
        create_process()
    elif option == "2":
        execute_next_process()
    elif option == "3":
        execute_specific_process()
    elif option == "4":
        save_process_list()
    elif option == "5":
        load_process_list()
    elif option == "0":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

#gg