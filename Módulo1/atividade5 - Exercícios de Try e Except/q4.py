try:
    with open('dados.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Arquivo criado com sucesso")