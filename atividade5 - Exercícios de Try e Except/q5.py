def verificarNumero():
    try:
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print("Par")
        else:
            print("Impar")
    except Exception as erro:
        print(f"Erro identificado: {erro}")


verificarNumero()