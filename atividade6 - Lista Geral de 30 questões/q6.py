def contar_caracteres(frase):
    contador = 0
    for letra in frase:
        contador += 1
    return contador


frase = input("Digite algo que o programa irá contar o numero de caracteres: ")
print(contar_caracteres(frase))