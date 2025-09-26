class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo


    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        elif valor == 0:
            print("Não é possível adicionar valores nulos!")
        else:
            print("Valores negativos não são aceitos!")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else: 
            print("Saldo insuficiente para resgate.")

    @property
    def saldo(self):
        return self.__saldo


conta1 = ContaBancaria("André", 500)

conta1.depositar(30)
print(conta1.saldo)
conta1.sacar(700)
        