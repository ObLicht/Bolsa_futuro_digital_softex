from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    @abstractmethod
    def detalhes_de_cadastro(self):
        pass

class Cliente(Pessoa):
    def __init__(self, id, nome, data_cadastro):
        super().__init__(id, nome)
        self.data_cadastro = data_cadastro

    def detalhes_de_cadastro(self):
        print(f"Cliente: {self.nome} - ID: {self.id} - Cadastrado em: {self.data_cadastro}")

class Fornecedor(Pessoa):
    def __init__(self, id, nome, cnpj):
        super().__init__(id, nome)
        self.cnpj = cnpj

    def detalhes_de_cadastro(self):
        print(f"Fornecedor: {self.nome} - ID: {self.id} - CNPJ: {self.cnpj}")

def exibir_detalhes(pessoas: list[Pessoa]):
    for pessoa in pessoas:
        pessoa.detalhes_de_cadastro()

c1 = Cliente(2212, "Anya", "27/09/2025")
f1 = Fornecedor(2804, "André", "78.787.878/0001-00")

lista_pessoas = [c1, f1]

exibir_detalhes(lista_pessoas)
