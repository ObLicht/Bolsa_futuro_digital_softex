def somarElementos(lista):
    soma = sum(lista)
    return soma

lista = []

print("Digite uma lista de 5 números inteiros:")
for i in range(5):
    numero = int(input())
    lista.append(numero)

print(f"A soma dos elementos da lista é: {somarElementos(lista)}")