import os

# Superclasse Process
class Process:
    def __init__(self, pid):
        self.pid = pid

    def execute(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

# Subclasse ComputingProcess
class ComputingProcess(Process):
    def __init__(self, pid, expression):
        super().__init__(pid)
        self.expression = expression

    def execute(self):
        try:
            result = eval(self.expression)
            print(f"Resultado da expressão '{self.expression}': {result}")
        except Exception as e:
            print(f"Erro ao executar a expressão: {e}")

# Subclasse WritingProcess
class WritingProcess(Process):
    def __init__(self, pid, expression):
        super().__init__(pid)
        self.expression = expression

    def execute(self):
        with open("computation.txt", "a") as file:
            file.write(self.expression + "\n")
        print(f"Expressão '{self.expression}' gravada no arquivo.")

# Subclasse ReadingProcess
class ReadingProcess(Process):
    def __init__(self, pid, process_list):
        super().__init__(pid)
        self.process_list = process_list

    def execute(self):
        if not os.path.exists("computation.txt"):
            print("Arquivo computation.txt não encontrado.")
            return

        with open("computation.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            self.process_list.append(ComputingProcess(len(self.process_list) + 1, line))
        open("computation.txt", "w").close()  # Limpa o arquivo
        print("Processos de cálculo carregados do arquivo e arquivo limpo.")

# Subclasse PrintingProcess
class PrintingProcess(Process):
    def __init__(self, pid, process_list):
        super().__init__(pid)
        self.process_list = process_list

    def execute(self):
        if not self.process_list:
            print("A lista de processos está vazia.")
            return

        print("Lista de Processos:")
        for process in self.process_list:
            print(f"PID: {process.pid}, Tipo: {type(process).__name__}")

# Funções principais
def criar_processo(process_list, pid):
    print("Selecione o tipo de processo: 1. Cálculo, 2. Gravação, 3. Leitura, 4. Impressão")
    tipo = int(input("Tipo: "))

    if tipo == 1:
        expression = input("Digite a expressão (ex: 5 + 3): ")
        process_list.append(ComputingProcess(pid, expression))
    elif tipo == 2:
        expression = input("Digite a expressão para gravar: ")
        process_list.append(WritingProcess(pid, expression))
    elif tipo == 3:
        process_list.append(ReadingProcess(pid, process_list))
    elif tipo == 4:
        process_list.append(PrintingProcess(pid, process_list))
    else:
        print("Tipo de processo inválido.")

def executar_proximo(process_list):
    if process_list:
        process = process_list.pop(0)
        process.execute()
    else:
        print("Nenhum processo na fila para executar.")

def executar_processo_especifico(process_list):
    pid = int(input("Digite o PID do processo a ser executado: "))
    for i, process in enumerate(process_list):
        if process.pid == pid:
            process.execute()
            del process_list[i]  # Remove o processo executado
            return
    print("Processo não encontrado.")

def salvar_processos(process_list):
    with open("process_pool.txt", "w") as file:
        for process in process_list:
            file.write(f"{process.pid},{type(process).__name__}\n")
    print("Fila de processos salva em process_pool.txt.")

def carregar_processos(process_list):
    if not os.path.exists("process_pool.txt"):
        print("Arquivo process_pool.txt não encontrado.")
        return

    with open("process_pool.txt", "r") as file:
        for line in file:
            pid, process_type = line.strip().split(",")
            pid = int(pid)
            if process_type == "ComputingProcess":
                expression = input(f"Digite a expressão para o PID {pid}: ")
                process_list.append(ComputingProcess(pid, expression))
            elif process_type == "WritingProcess":
                expression = input(f"Digite a expressão para o PID {pid}: ")
                process_list.append(WritingProcess(pid, expression))
            elif process_type == "ReadingProcess":
                process_list.append(ReadingProcess(pid, process_list))
            elif process_type == "PrintingProcess":
                process_list.append(PrintingProcess(pid, process_list))
    print("Fila de processos carregada de process_pool.txt.")

# Menu principal
def main():
    process_list = []
    pid_counter = 1

    while True:
        print("\nMenu:")
        print("1. Criar processo")
        print("2. Executar próximo")
        print("3. Executar processo específico")
        print("4. Salvar processos")
        print("5. Carregar processos")
        print("6. Sair")

        opcao = int(input("Selecione uma opção: "))

        if opcao == 1:
            criar_processo(process_list, pid_counter)
            pid_counter += 1
        elif opcao == 2:
            executar_proximo(process_list)
        elif opcao == 3:
            executar_processo_especifico(process_list)
        elif opcao == 4:
            salvar_processos(process_list)
        elif opcao == 5:
            carregar_processos(process_list)
        elif opcao == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
