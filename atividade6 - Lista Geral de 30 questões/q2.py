def verificarNumero(numero):
    if numero > 0:
        print("É positivo")
    elif numero < 0:
        print("É negativo")
    else:
        print("É zero")

numero = int(input("Digite um número: "))

verificarNumero(numero)