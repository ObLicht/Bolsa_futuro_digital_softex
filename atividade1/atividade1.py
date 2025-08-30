def iniciarComA(palavra, contadores):
    if palavra.startswith("a"):
        contadores["comeca_com_a"] += 1
        print("Começa com A", end=", ")

def verificarPalindromo(palavra, contadores):
    if palavra == palavra[::-1]:
        contadores["palindromos"] += 1
        print("É um Palíndromo", end=", ")

def verificarTamanho(palavra, contadores):
    if len(palavra) > 7:
        contadores["palavras_longas"] += 1
        print("Palavra Longa")
    else:
        contadores["comuns"] += 1
        print("Palavra Comum")

contadores = {
    "comuns": 0,
    "palindromos": 0,
    "comeca_com_a": 0,
    "palavras_longas": 0
}

palavras = input("Digite palavras separadas por espaços: ")
listaPalavras = palavras.split()

for palavra in listaPalavras:
    print(f"{palavra} ->", end=" ")
    iniciarComA(palavra, contadores)
    verificarPalindromo(palavra, contadores)
    verificarTamanho(palavra, contadores)
    print("\n")

print("|| Resumo ||")
print(f"Palavras que começam com A: {contadores['comeca_com_a']}")
print(f"Palíndromos: {contadores['palindromos']}")
print(f"Palavras longas: {contadores['palavras_longas']}")
print(f"Palavras comuns: {contadores['comuns']}")
