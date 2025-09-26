class Produto:
    def  __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco   
        else:
            print("O preço deve ser um valor positivo!")

#testes
sabao = Produto("Palmolive", 3.50)
print(sabao.preco)
sabao.preco = 3.25
print(sabao.preco)
sabao.preco = -3