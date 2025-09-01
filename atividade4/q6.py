
def contar_elementos(lista):
    if lista == []:
        return 0
    else:
        return 1 + contar_elementos(lista[1:])

lista_teste = [1,3,6,52,9,5,4,1,0]

print(contar_elementos(lista_teste))