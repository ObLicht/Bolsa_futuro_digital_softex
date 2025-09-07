import math

pontos = [(3, 4), (5, 12), (8, 15)]

for x, y in pontos:
    distancia = math.sqrt(x**2 + y**2)
    print(f"Ponto ({x}, {y}) -> Distância até a origem: {distancia:.2f}")
