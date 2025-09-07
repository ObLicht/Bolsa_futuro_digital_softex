def contarElementos(palavra):
    frequencia = {}
    for letra in palavra:
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1
    return frequencia

palavra = "hello"
resultado = contarElementos(palavra)
print(resultado)
