frase = input("Escreva uma palavra ou frase para verificação: ").lower()
frase.replace(" ","")

if frase == frase[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")
