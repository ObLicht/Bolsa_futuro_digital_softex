class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome} - Salário: {self.salario} - Departamento: {self.departamento}")

g = Gerente("Luis", 1518, "Organização de Projetos")
g.mostrar_informacoes()

