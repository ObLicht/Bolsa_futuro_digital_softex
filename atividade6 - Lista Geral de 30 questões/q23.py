menu = {
    "Encerrar programa" : 0,
    "Ver estoque" : 1,
    "Adicionar Item" : 2,
    "Remover Item" : 3
}

entrada = -1

while (entrada != 0):
    print(menu)
    try:
        entrada = int(input("Digite a opção desejada: "))
        for chave,valor in menu.items():
            if valor == entrada:
                print(f"Dados do menu: {chave}\n")
    except:
        print("Número não encontrado") 
