def verificarPalindromo(palavra):
    if palavra == palavra[::-1]:
        print("É Palíndromo")
    else:
        print("Não é Palíndromo")

palavra = input("Digire uma palavra para verificação: ")

verificarPalindromo(palavra)