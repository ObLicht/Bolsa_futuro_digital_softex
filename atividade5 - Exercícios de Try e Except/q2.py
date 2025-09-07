class ValorInvalidoErro(Exception):
    pass

def depositar(valor):
    try:
        if valor >= 0:
            print("Valor adicionado")
        else:
            raise ValorInvalidoErro
    except ValorInvalidoErro:
        print("Não é aceito valores negativos")

depositar(-20)
depositar(100)
