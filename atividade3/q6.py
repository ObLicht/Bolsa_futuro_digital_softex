def mostrar_tabuleiro(tab):
    for linha in range(3):
        for coluna in range(3):
            print(tab[(linha, coluna)], end=" ")
        print()
    print()

def verificar_vitoria(tab):
    for linha in range(3):
        if tab[(linha,0)] == tab[(linha,1)] == tab[(linha,2)] != "-":
            return tab[(linha,0)]
    for coluna in range(3):
        if tab[(0,coluna)] == tab[(1,coluna)] == tab[(2,coluna)] != "-":
            return tab[(0,coluna)]
    if tab[(0,0)] == tab[(1,1)] == tab[(2,2)] != "-":
        return tab[(0,0)]
    if tab[(0,2)] == tab[(1,1)] == tab[(2,0)] != "-":
        return tab[(0,2)]
    return None

tabuleiro = {
    (0,0): "-", (0,1): "-", (0,2): "-",
    (1,0): "-", (1,1): "-", (1,2): "-",
    (2,0): "-", (2,1): "-", (2,2): "-"
}

jogador1 = 0
jogador2 = 0

mostrar_tabuleiro(tabuleiro)

while True:
    posicao = input("Qual a posição? (Digite 123 para encerrar) ")
    if posicao == "123":
        break
    try:
        partes = posicao.split(",")
        linha = int(partes[0])
        coluna = int(partes[1])
        valor = input("Qual o valor (X ou O): ").upper()
        if tabuleiro.get((linha, coluna), None) == "-":
            tabuleiro[(linha, coluna)] = valor
        else:
            print("Posição ocupada")
            continue
    except:
        print("Inválido, tente novamente")
        continue

    mostrar_tabuleiro(tabuleiro)

    vencedor = verificar_vitoria(tabuleiro)
    if vencedor == "X":
        print("Jogador X venceu!")
        jogador1 += 1
        break
    elif vencedor == "O":
        print("Jogador O venceu!")
        jogador2 += 1
        break

print(f"Placar final: Jogador X: {jogador1}, Jogador O: {jogador2}")
