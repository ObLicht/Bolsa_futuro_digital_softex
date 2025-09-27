from abc import ABC, abstractmethod 

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        area = self.largura * self.altura
        return area
        
r = Retangulo(2, 5)
print(r.calcular_area())
