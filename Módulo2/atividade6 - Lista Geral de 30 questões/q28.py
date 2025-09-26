def gerar_lista():
    lista = []
    print("Digite os elementos da lista: ")
    for i in range(1,11):
        numero = int(input())
        lista.append(numero)
    return lista

def verificar_numeros(lista):
    contagem = 0
    for numero in lista:
        if numero > 0:
            contagem += 1
        
    if contagem == (len(lista)):
        print("A lista é composta apenas de números positivos")
    else:
        print("A lista contém números negativos")

lista_usuario = gerar_lista()

verificar_numeros(lista_usuario)