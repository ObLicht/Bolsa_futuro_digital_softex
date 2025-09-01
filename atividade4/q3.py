
lista= [1,23,4,5,6,43,56,7,8,44,89]

n = len(lista)
for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j] < lista[j + 1]: 
            lista[j], lista[j + 1] = lista[j + 1], lista[j]


print(lista)  