from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcular_bonus(self):
        pass

class Gerente(Funcionario):
    def calcular_bonus(self):
        print("O gerente tem R$ 200,00 de bonificação")

class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        print("O Desenvolvedor tem R$ 500,00 de bonificação")

gerente1 = Gerente()
dev1 = Desenvolvedor()
gerente1.calcular_bonus()
dev1.calcular_bonus()