class Estoque:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome              
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_produto(self):
        produto_estoque = {
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade
        }
        return produto_estoque  
    def total_em_estoque(self):
        total = self.preco * self.quantidade
        print(f"Total em estoque de {self.nome}: R${total:.2f}")

produto = Estoque("Sabão", 5.99, 13)

dados_produto = produto.adicionar_produto()
print(dados_produto)

produto.total_em_estoque()
