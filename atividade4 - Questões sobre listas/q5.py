
def calcular_potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * calcular_potencia(base, expoente - 1)

print(calcular_potencia(2,3))
   
