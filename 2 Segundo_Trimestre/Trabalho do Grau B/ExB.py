import os

# Classe base
class Process:
    def __init__(self, pid):
        self.pid = pid

    def execute(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

# Subclasses específicas
class ComputingProcess(Process):
    def __init__(self, pid, expression):
        super().__init__(pid)
        self.expression = expression

    def execute(self):
        try:
            result = eval(self.expression)
            print(f"Resultado do cálculo {self.expression} = {result}")
        except Exception as e:
            print(f"Erro na expressão: {e}")

class WritingProcess(Process):
    def __init__(self, pid, expression):
        super().__init__(pid)
        self.expression = expression

    def execute(self):
        with open("computation.txt", "a") as file:
            file.write(self.expression + "\n")
        print(f"Expressão '{self.expression}' gravada em computation.txt.")

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
            if line:
                self.process_list.append(ComputingProcess(len(self.process_list) + 1, line))

        open("computation.txt", "w").close()  # Limpa o arquivo
        print("Arquivo computation.txt lido e expressões carregadas como processos de cálculo.")

class PrintingProcess(Process):
    def __init__(self, pid, process_list):
        super().__init__(pid)
        self.process_list = process_list

    def execute(self):
        print("Pool de processos:")
        for process in self.process_list:
            print(f"PID: {process.pid}, Tipo: {type(process).__name__}")

# Classe Sistema
class System:
    def __init__(self):
        self.process_list = []
        self.next_pid = 1

    def create_process(self):
        print("1. Processo de cálculo\n2. Processo de gravação\n3. Processo de leitura\n4. Processo de impressão")
        choice = int(input("Selecione o tipo de processo: "))
        if choice == 1:
            expression = input("Digite a expressão (ex: 2 + 2): ")
            self.process_list.append(ComputingProcess(self.next_pid, expression))
        elif choice == 2:
            expression = input("Digite a expressão para gravar: ")
            self.process_list.append(WritingProcess(self.next_pid, expression))
        elif choice == 3:
            self.process_list.append(ReadingProcess(self.next_pid, self.process_list))
        elif choice == 4:
            self.process_list.append(PrintingProcess(self.next_pid, self.process_list))
        else:
            print("Opção inválida.")
            return
        print(f"Processo com PID {self.next_pid} criado.")
        self.next_pid += 1

    def execute_next(self):
        if not self.process_list:
            print("Nenhum processo para executar.")
            return
        process = self.process_list.pop(0)
        process.execute()

    def execute_specific(self):
        pid = int(input("Digite o PID do processo a ser executado: "))
        for i, process in enumerate(self.process_list):
            if process.pid == pid:
                process.execute()
                self.process_list.pop(i)
                return
        print("Processo não encontrado.")

    def save_processes(self):
        with open("process_pool.txt", "w") as file:
            for process in self.process_list:
                file.write(f"{process.pid},{type(process).__name__}\n")
        print("Fila de processos salva em process_pool.txt.")

    def load_processes(self):
        if not os.path.exists("process_pool.txt"):
            print("Arquivo process_pool.txt não encontrado.")
            return
        with open("process_pool.txt", "r") as file:
            lines = file.readlines()
        self.process_list = []
        for line in lines:
            pid, process_type = line.strip().split(",")
            pid = int(pid)
            if process_type == "ComputingProcess":
                self.process_list.append(ComputingProcess(pid, "0 + 0"))
            elif process_type == "WritingProcess":
                self.process_list.append(WritingProcess(pid, ""))
            elif process_type == "ReadingProcess":
                self.process_list.append(ReadingProcess(pid, self.process_list))
            elif process_type == "PrintingProcess":
                self.process_list.append(PrintingProcess(pid, self.process_list))
        print("Fila de processos carregada de process_pool.txt.")

# Menu principal
def main():
    system = System()
    while True:
        print("\n1. Criar processo\n2. Executar próximo\n3. Executar processo específico\n4. Salvar processos\n5. Carregar processos\n6. Sair")
        choice = int(input("Selecione uma opção: "))
        if choice == 1:
            system.create_process()
        elif choice == 2:
            system.execute_next()
        elif choice == 3:
            system.execute_specific()
        elif choice == 4:
            system.save_processes()
        elif choice == 5:
            system.load_processes()
        elif choice == 6:
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
