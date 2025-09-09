class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __repr__(self):
        return f"'{self.titulo}' de {self.autor} ({self.ano})"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def buscar_por_autor(self, autor):
        autor_normalizado = self.normalizar_texto(autor)
        return [
            livro for livro in self.livros
            if self.normalizar_texto(livro.autor) == autor_normalizado
        ]

    @staticmethod
    def normalizar_texto(texto):
        return ' '.join(texto.lower().split())
