#####################################################baze inicial
import pickle # modelo para salva da dos do projeto

# Classe base para Process
class Process:
    def __init__(self, pid):
        self.pid = pid

    def execute(self):
        pass  # O método execute será implementado nas subclasses

# Subclasse para processo de cálculo
class ComputingProcess(Process):
    def __init__(self, pid, expression):
        super().__init__(pid)
        self.expression = expression

    def execute(self):
        operands = self.expression.split()
        if len(operands) == 3:
            op1, operator, op2 = operands
            try:
                op1, op2 = float(op1), float(op2)
                if operator == '+':
                    result = op1 + op2
                elif operator == '-':
                    result = op1 - op2
                elif operator == '*':
                    result = op1 * op2
                elif operator == '/':
                    result = op1 / op2
                else:
                    print("Operador desconhecido")
                    return
                print(f"Resultado da expressão {self.expression}: {result}")
            except ValueError:
                print("Erro: operandos inválidos")
        else:
            print("Expressão malformada")

# Subclasse para processo de gravação
class WritingProcess(Process):
    def __init__(self, pid, expression):
        super().__init__(pid)
        self.expression = expression

    def execute(self):
        with open("computation.txt", "a") as file:
            file.write(self.expression + "\n")
        print(f"Expressão '{self.expression}' gravada no arquivo.")

# Subclasse para processo de leitura
class ReadingProcess(Process):
    def __init__(self, pid, process_list):
        super().__init__(pid)
        self.process_list = process_list

    def execute(self):
        try:
            with open("computation.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    expression = line.strip()
                    if expression:
                        new_pid = len(self.process_list) + 1
                        self.process_list.append(ComputingProcess(new_pid, expression))
            open("computation.txt", "w").close()  # Limpa o arquivo
            print("Arquivo lido e processos de cálculo criados.")
        except FileNotFoundError:
            print("Arquivo computation.txt não encontrado.")

# Subclasse para processo de impressão
class PrintingProcess(Process):
    def __init__(self, pid, process_list):
        super().__init__(pid)
        self.process_list = process_list

    def execute(self):
        print("Fila de processos:")
        for process in self.process_list:
            print(f"PID: {process.pid}, Tipo: {type(process).__name__}")

###################################################################### Adicionar a funcionalidade de "Criar processo

# Classe base para Process e subclasses (código anterior)

# Lista de processos
process_list = []

# Função para criar um novo processo
def create_process():
    print("\nSelecione o tipo de processo para criar:")
    print("1 - ComputingProcess (Processo de Cálculo)")
    print("2 - WritingProcess (Processo de Gravação)")
    print("3 - ReadingProcess (Processo de Leitura)")
    print("4 - PrintingProcess (Processo de Impressão)")

    choice = input("Digite o número correspondente ao tipo de processo: ")
    
    # Geração do PID automático
    pid = len(process_list) + 1

    if choice == "1":
        # Criar um ComputingProcess
        expression = input("Digite a expressão (ex: 5 + 3): ")
        process = ComputingProcess(pid, expression)
        process_list.append(process)
        print(f"Processo de Cálculo criado com PID {pid} e adicionado à lista.")
    
    elif choice == "2":
        # Criar um WritingProcess
        expression = input("Digite a expressão para gravar (ex: 5 * 2): ")
        process = WritingProcess(pid, expression)
        process_list.append(process)
        print(f"Processo de Gravação criado com PID {pid} e adicionado à lista.")
    
    elif choice == "3":
        # Criar um ReadingProcess
        process = ReadingProcess(pid, process_list)
        process_list.append(process)
        print(f"Processo de Leitura criado com PID {pid} e adicionado à lista.")
    
    elif choice == "4":
        # Criar um PrintingProcess
        process = PrintingProcess(pid, process_list)
        process_list.append(process)
        print(f"Processo de Impressão criado com PID {pid} e adicionado à lista.")
    
    else:
        print("Opção inválida. Por favor, tente novamente.")

# Menu principal para teste
while True:
    print("\n--- Menu ---")
    print("1 - Criar processo")
    print("0 - Sair")
    option = input("Escolha uma opção: ")
    
    if option == "1":
        create_process()
    elif option == "0":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

########################################## Executar próximo
# Função para executar o próximo processo na fila
def execute_next_process():
    if not process_list:
        print("A fila de processos está vazia.")
        return

    # Executa o processo do índice zero
    next_process = process_list[0]
    print(f"\nExecutando o processo com PID {next_process.pid}...")
    next_process.execute()

    # Remove o processo executado e atualiza a lista
    process_list.pop(0)
    print("Processo executado e removido da lista.")

# Menu atualizado para incluir a opção de executar o próximo processo
while True:
    print("\n--- Menu ---")
    print("1 - Criar processo")
    print("2 - Executar próximo processo")
    print("0 - Sair")
    option = input("Escolha uma opção: ")

    if option == "1":
        create_process()
    elif option == "2":
        execute_next_process()
    elif option == "0":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
################################################################# Executar processo específico:

#apagar depois 