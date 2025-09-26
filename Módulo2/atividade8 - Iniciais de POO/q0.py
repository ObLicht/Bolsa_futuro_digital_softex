class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def __str__(self):
        return f"{self.marca} - {self.ano}"

celta = Carro("Chevrolet", 2012)
print(celta)