class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = nota
    
    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, nova_nota):
        if nova_nota >= 0 and nova_nota <= 10:
            self.__nota = nova_nota
        else:
            print("Nota inválida")

aluno1 = Aluno("Carlos", 8.6)
print(aluno1.nota)
aluno1.nota = 7.3
print(aluno1.__dict__)
aluno1.nota = 11