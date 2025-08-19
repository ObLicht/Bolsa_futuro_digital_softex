
def contarPalavras(frase):
    palavras = frase.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem
        
frase = input("Escreva uma frase para verificação: ").lower()

frequencia = contarPalavras(frase)
print(frequencia)
