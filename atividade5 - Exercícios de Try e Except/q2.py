def depositar(valor):
    try:
        if valor >= 0:
            print("Valor adicionado")
    except Exception: 
        print("Não é aceito números negativos: ValorInvalidoErro")

depositar(-20)