lista = []
for i in range(5):
    numero = int(input("Digite um número: "))
    lista.append(numero)

lista.sort()
nova_lista = sorted(lista)

numero_escolhido = int(input("Qual número deseja encontrar? "))

encontrado = False
for elemento in lista:
    if elemento == numero_escolhido:
        encontrado = True

if encontrado:
    print("O número está na lista ")
else:
    print("O número não está na lista ")
