from abc import ABC, abstractmethod

class Arquivo(ABC):
    @abstractmethod
    def abrir(self):
        pass

class ArquivoTexto(Arquivo):
    def abrir(self):
        print("Arquivo de texto aberto")

class ArquivoImagem(Arquivo):
    def abrir(self):
        print("Acessando Imagem")

txt = ArquivoTexto()
img = ArquivoImagem()
txt.abrir()
img.abrir()