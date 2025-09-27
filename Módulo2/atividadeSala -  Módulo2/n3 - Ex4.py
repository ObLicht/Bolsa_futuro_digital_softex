from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, rodas):
        self.rodas = rodas

    @property
    def rodas(self):
        return self.rodas

    @abstractmethod
    def acelerar(self):
        pass

class Carro(Veiculo):
    def __init__(self, rodas):
        super().__init__(rodas)

    def acelerar(self):
        return super().acelerar()

class Moto(Veiculo):
    def __init__(self, rodas):
        super().__init__(rodas)
    