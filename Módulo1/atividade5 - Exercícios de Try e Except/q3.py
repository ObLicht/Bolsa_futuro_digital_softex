lista = [10,20,30,40]

try:
    indice = int(input("Qual o índice? "))
    print(lista[indice])
except IndexError:
    print(f"Esse índice não existe na lista")