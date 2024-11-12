import os

# Classe base
class Process:
    def __init__(self, pid):
        self.pid = pid

    def execute(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")

# Subclasse de processo de cálculo
class ComputingProcess(Process):
    def __init__(self, pid, expression):
        super().__init__(pid)
        self.expression = expression

    def execute(self):
        try:
            result = eval(self.expression)
            print(f"Processo {self.pid}: Resultado do cálculo {self.expression} = {result}")
        except Exception as e:
            print(f"Erro ao executar o cálculo: {e}")

# Subclasse de processo de gravação
class WritingProcess(Process):
    def execute(self):
        with open("computation.txt", "a") as file:
            file.write(f"Processo {self.pid}: {self.expression}\n")
        print(f"Processo {self.pid}: Gravação concluída.")

# Subclasse de processo de leitura
class ReadingProcess(Process):
    def __init__(self, pid, process_list):
        super().__init__(pid)
        self.process_list = process_list

    def execute(self):
        if not os.path.exists("computation.txt"):
            print("Arquivo de computações não encontrado.")
            return

        with open("computation.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            expression = line.strip()
            new_process = ComputingProcess(len(self.process_list) + 1, expression)
            self.process_list.append(new_process)

        open("computation.txt", "w").close()  # Limpa o arquivo
        print(f"Processo {self.pid}: Leitura e criação de novos processos concluída.")

# Subclasse de processo de impressão
class PrintingProcess(Process):
    def __init__(self, pid, process_list):
        super().__init__(pid)
        self.process_list = process_list

    def execute(self):
        print("Fila de processos:")
        for process in self.process_list:
            print(f"PID: {process.pid}, Tipo: {type(process).__name__}")

# Classe para gerenciar o sistema
class System:
    def __init__(self):
        self.process_list = []
        self.next_pid = 1

    def create_process(self):
        process_type = input("Escolha o tipo de processo (1: Cálculo, 2: Gravação, 3: Leitura, 4: Impressão): ")
        if process_type == "1":
            expression = input("Digite a expressão a ser calculada: ")
            new_process = ComputingProcess(self.next_pid, expression)
        elif process_type == "2":
            new_process = WritingProcess(self.next_pid)
        elif process_type == "3":
            new_process = ReadingProcess(self.next_pid, self.process_list)
        elif process_type == "4":
            new_process = PrintingProcess(self.next_pid, self.process_list)
        else:
            print("Tipo de processo inválido.")
            return

        self.process_list.append(new_process)
        self.next_pid += 1
        print(f"Processo {new_process.pid} criado com sucesso.")

    def execute_next(self):
        if not self.process_list:
            print("Nenhum processo na fila para executar.")
            return

        process = self.process_list.pop(0)
        process.execute()
        print(f"Processo {process.pid} executado e removido da fila.")

    def execute_specific(self):
        pid = int(input("Digite o PID do processo a ser executado: "))
        for i, process in enumerate(self.process_list):
            if process.pid == pid:
                process.execute()
                self.process_list.pop(i)
                print(f"Processo {process.pid} executado e removido da fila.")
                return
        print("Processo não encontrado.")

    def save_processes(self):
        with open("process_pool.txt", "w") as file:
            for process in self.process_list:
                file.write(f"{process.pid},{type(process).__name__}\n")
        print("Fila de processos salva em arquivo.")

    def load_processes(self):
        if not os.path.exists("process_pool.txt"):
            print("Arquivo de processos não encontrado.")
            return

        with open("process_pool.txt", "r") as file:
            lines = file.readlines()

        self.process_list.clear()
        for line in lines:
            pid, process_type = line.strip().split(",")
            if process_type == "ComputingProcess":
                expression = input(f"Digite a expressão para o processo {pid}: ")
                self.process_list.append(ComputingProcess(int(pid), expression))
            elif process_type == "WritingProcess":
                self.process_list.append(WritingProcess(int(pid)))
            elif process_type == "ReadingProcess":
                self.process_list.append(ReadingProcess(int(pid), self.process_list))
            elif process_type == "PrintingProcess":
                self.process_list.append(PrintingProcess(int(pid), self.process_list))

        print("Fila de processos carregada do arquivo.")

# Menu principal
def main():
    system = System()
    while True:
        print("\n1: Criar processo\n2: Executar próximo\n3: Executar processo específico\n4: Salvar fila\n5: Carregar fila\n6: Sair")
        choice = input("Escolha uma opção: ")
        if choice == "1":
            system.create_process()
        elif choice == "2":
            system.execute_next()
        elif choice == "3":
            system.execute_specific()
        elif choice == "4":
            system.save_processes()
        elif choice == "5":
            system.load_processes()
        elif choice == "6":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
