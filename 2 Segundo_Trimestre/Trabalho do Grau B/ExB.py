import os

class Process:
    def __init__(self, pid):
        self.pid = pid

    def execute(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses")

class ComputingProcess(Process):
    def __init__(self, pid, expression):
        super().__init__(pid)
        self.expression = expression

    def execute(self):
        op1, operator, op2 = self.expression.split()
        op1, op2 = int(op1), int(op2)
        if operator == '+':
            result = op1 + op2
        elif operator == '-':
            result = op1 - op2
        elif operator == '*':
            result = op1 * op2
        elif operator == '/':
            result = op1 / op2
        print(f"Resultado da expressão {self.expression}: {result}")

class WritingProcess(Process):
    def execute(self):
        with open("computation.txt", "a") as f:
            f.write(f"{self.pid}\n")
        print(f"Processo de gravação executado para PID: {self.pid}")

class ReadingProcess(Process):
    def __init__(self, pid, process_pool):
        super().__init__(pid)
        self.process_pool = process_pool

    def execute(self):
        if os.path.exists("computation.txt"):
            with open("computation.txt", "r") as f:
                for line in f:
                    pid = line.strip()
                    self.process_pool.append(ComputingProcess(pid, "2 + 3"))
            open("computation.txt", "w").close()  
        print("Processo de leitura executado")

