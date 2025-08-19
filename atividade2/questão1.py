
frase = input("Escreva uma frase: ").lower()
vogais = list("aeiou")

contagemVogal = 0
contagemConsoante = 0

for letra in frase:
    if letra.isalpha():
        if letra in vogais:
            contagemVogal += 1
        else:
            contagemConsoante += 1

print(f"Vogais: {contagemVogal}")
print(f"Consoante: {contagemConsoante}")