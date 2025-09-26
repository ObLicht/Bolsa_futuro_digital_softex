pessoas = {
    "Ana" : 21,
    "Arthur" : 24,
    "Carlos" :33
}

for i, (nome, idade) in enumerate(pessoas.items()):
    print(f"{i}: {nome} tem {idade} anos.")