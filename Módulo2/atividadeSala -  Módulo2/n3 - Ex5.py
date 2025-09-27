class DispositivoEletronico:
    def ligar(self):
        print("Ligado")
    
    def desligar(self):
        print("Desligado")
    
class Computador(DispositivoEletronico):
    def instalar_software(self):
        print("Instalando..")

class Notebook(Computador):
    def verificar_bateria(self):
        print("Bateria em X%")

note = Notebook()
note.ligar()
note.desligar()
note.instalar_software()
note.verificar_bateria()