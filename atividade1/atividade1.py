
def iniciarComA(palavra):
    global contagemA
    if palavra.startswith("a"):
        contagemA += 1
        print("Começa com A", end=", ")
        
def verificarPalindromo(palavra):
    global contagemPalindromos
    if palavra == palavra[::-1]:
        contagemPalindromos += 1
        print("É um Palíndromo", end=", ")
        
def verificarTamanho(palavra):
    global contagemPalavraLonga, contagemComuns
    if len(palavra) > 7:
        contagemPalavraLonga += 1
        print("Palavra Longa")
    else:
        contagemComuns += 1
        print("Palavra Comum")

contagemComuns = 0
contagemPalindromos = 0
contagemA = 0
contagemPalavraLonga = 0

palavras = input("Digite palavras separadas por espaços:")

listaPalavras = palavras.split()

for palavra in listaPalavras:
    print(f"{palavra} ->", end=" ")
    iniciarComA(palavra)
    verificarPalindromo(palavra)
    verificarTamanho(palavra)
    print("\n")

print("|| Resumo ||")
print(f"Palavras que começam com A: {contagemA}\n")
print(f"Palíndromos: {contagemPalindromos}\n")
print(f"Palavras longas: {contagemPalavraLonga}\n")
print(f"Palavras Comuns: {contagemComuns}\n")