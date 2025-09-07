def verificarMaior(lista):
    maior = max(lista)
    print(f"O maior número é: {maior}")

print("Digite os elementos da lista: ")
lista = []
for i in range(1,11):
    numero = int(input())
    lista.append(numero)

print(lista)
verificarMaior(lista)