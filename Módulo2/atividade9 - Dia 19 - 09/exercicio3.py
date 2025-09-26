class Jogador:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

class Time:
    def __init__(self, jogador: Jogador):
        self.jogador = jogador
        
    def contarJogadores(self):
        listaTime = []
        listaTime.append(self.jogador)  
        return listaTime  
    
    def mostrarJogadores(self):
        print(f"Nome: {self.jogador.nome} - Número: {self.jogador.numero}")

jogador1 = Jogador("Kaiser", 10)
time1 = Time(jogador1)
time1.contarJogadores()
time1.mostrarJogadores()
