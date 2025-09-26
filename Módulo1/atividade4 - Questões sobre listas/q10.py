def fatorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado


lista_usuario = []

print("Digite dez números para sua lista: ")
for i in range(10):
    digito = int(input())
    lista_usuario.append(digito)

print("Lista original:", lista_usuario)

lista_usuario.sort()
print("Lista ordenada:", lista_usuario)

procurar = int(input("Qual valor deseja procurar? "))

if procurar in lista_usuario:
    print("O número foi encontrado na lista! ")
    print(f"Fatorial de {procurar} = {fatorial(procurar)}")
else:
    print("O número não está na lista! ")
