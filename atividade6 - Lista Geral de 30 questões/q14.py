def gerarTabuada(numero):
    for i in range(1,6):
        multiplicacao = i * numero
        print(f"{i} X {numero} = {multiplicacao}")

numero = int(input("Digite um número: "))

gerarTabuada(numero)