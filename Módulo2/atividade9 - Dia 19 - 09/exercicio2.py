class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
    
class ContaBancaria:
    def __init__(self, numero, cliente : Cliente):
        self.numero = numero
        self.cliente = cliente

    def mostrarDadosClientes(self):
        print(f"Cliente: {self.cliente.nome} - CPF: {self.cliente.cpf} - Número da Conta: {self.numero}")


cliente1 = Cliente("Lara", 12345678)
conta_cliente1 = ContaBancaria("111", cliente1)

conta_cliente1.mostrarDadosClientes()


    