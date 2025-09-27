from abc import ABC, abstractmethod

class Percurso(ABC):
    @abstractmethod
    def tempo_estimado(self):
        pass

class Cobranca(ABC):
    @abstractmethod
    def calcular_tarifa(self):
        pass

class Taxi(Percurso, Cobranca):
    def __init__(self, tempo):
        self.tempo = tempo

    def tempo_estimado(self):
        return self.tempo
    
    def calcular_tarifa(self):
        tarifa = self.tempo * 0.2
        return tarifa
    

taxi1 = Taxi(20)

print(taxi1.tempo_estimado())
print(taxi1.calcular_tarifa())