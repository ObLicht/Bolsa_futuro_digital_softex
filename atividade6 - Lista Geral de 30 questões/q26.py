def filtrar_pares(lista):
    lista_pares = []
    for elemento in lista:
        if elemento % 2 == 0:
            lista_pares.append(elemento)
    lista_pares.sort()
    return lista_pares

def gerar_lista():
    lista = []
    print("Digite os elementos da lista: ")
    for i in range(1,11):
        numero = int(input())
        lista.append(numero)
    return lista
    
lista_usuario = gerar_lista()
print(f"Lista com os pares ordenada: {filtrar_pares(lista_usuario)}")