def fibonacci_iterativo(n):
    sequencia = [0, 1]
    for i in range(2, n):
        sequencia.append(sequencia[i-1] + sequencia[i-2])
    return sequencia[:n]

valores = int(input("Quantos valores da sequência de Fibonacci deseja ver? "))

print("Iterativo:")
print(fibonacci_iterativo(valores))

print("---------------------------------------------------------------")

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

print("Recursivo:")
for i in range(valores):
    print(fibonacci_recursivo(i), end=" ")
