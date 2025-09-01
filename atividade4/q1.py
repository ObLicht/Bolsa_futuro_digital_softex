
elemento = int(input("Digite um valor: "))
existe = False
lista = [2,4,6,78,9,0,7,54,2,5,6]

for i in range(len(lista)):
    if elemento == lista[i]:
        existe = True


print(lista)
print(existe)