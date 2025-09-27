from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, saldo):
        self.saldo = saldo

    @abstractmethod
    def sacar(self):
        pass

    def verificar_saldo(self):
        print(f"O saldo atual é: {self.saldo}")

class ContaCorrente(ContaBancaria):
    def __init__(self, saldo):
        super().__init__(saldo)

    def sacar(self):
        print(f"Total a sacar: {self.saldo}")


c1 = ContaCorrente(150)
c2 = ContaCorrente(300)
c3 = ContaCorrente(200)
contas = [c1, c2, c3]

for conta in contas:
    conta.verificar_saldo()
    conta.sacar()