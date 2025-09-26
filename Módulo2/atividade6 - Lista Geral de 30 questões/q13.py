def classificar(numero):
    if numero < 10:
        print("Número pequeno")
    elif numero >= 10 and numero <= 50:
        print("Número médio")
    else:
        print("Número grande")
numero = int(input("Digite um número: "))

classificar(numero)