def criarAcronimo(frase):
    stopwords = {"de", "da", "do", "das", "dos", "e"}
    palavras = frase.lower().split()
    
    letras = [palavra[0].upper() for palavra in palavras if palavra not in stopwords]
    
    acronimo = "".join(letras)
    print(acronimo)

frase = input("Digite um curso/expressão: ")
criarAcronimo(frase)
