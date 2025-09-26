def contar_vogais(frase):
        contagem_vogais = 0
        vogais = list("aeiou")
        for letra in frase:
                if letra in vogais:
                        contagem_vogais += 1
        return contagem_vogais

inserir_frase = input("Digite uma palavra ou frase para contar vogais: ")

print(f"O número de vogais da palavra/frase é: {contar_vogais(inserir_frase)}")