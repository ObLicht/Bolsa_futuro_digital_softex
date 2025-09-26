def dividir(numero1, numero2):
    try:
            divisao = numero1 / numero2
            return divisao
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida"

print(dividir(10,5))
print(dividir(10,0))
print(dividir(5,2))