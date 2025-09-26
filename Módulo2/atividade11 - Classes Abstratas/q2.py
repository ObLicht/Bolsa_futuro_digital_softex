from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass
    
    @abstractmethod
    def frear(self):
        pass


class Carro(Veiculo):
    def acelerar(self):
        print("Acelerando carro")

    def frear(self):
        print("Freando carro")

class Moto(Veiculo):
    def acelerar(self):
        print("Acelerando Moto")

    def frear(self):
        print("Freando Moto")


c = Carro()
m = Moto()

c.acelerar()
c.frear()
m.acelerar()
m.frear()