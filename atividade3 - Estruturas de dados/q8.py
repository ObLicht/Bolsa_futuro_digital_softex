pontos_turisticos = {
    (-22.951916, -43.210466): "Cristo Redentor",
    (-12.989906, -38.513444): "Elevador Lacerda",
    (-7.231, -35.881): "Açude Velho"
}

latitude = float(input("Digite a latitude: "))
longitude = float(input("Digite a longitude: "))

coordenada = (latitude, longitude)

if coordenada in pontos_turisticos:
    print(pontos_turisticos[coordenada])
else:
    print("Não existe em nossos dados!")
