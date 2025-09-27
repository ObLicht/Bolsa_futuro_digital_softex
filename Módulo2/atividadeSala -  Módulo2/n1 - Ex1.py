class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som Genérico")
    

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)


    def emitir_som(self):
        print("Latido!")

animal = Animal("Tatu")
dog = Cachorro("Bola")
animal.emitir_som()
dog.emitir_som()