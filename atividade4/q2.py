lista_teste = [1,4,7,2,5,4,2,8,9,2]
contagem = 0
valor = int(input("Digite um valor: "))

for numero in lista_teste:
    if numero == valor:
        contagem += 1
    
print(contagem)