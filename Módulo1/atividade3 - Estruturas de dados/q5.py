
precos = {
    ("Camiseta", "M"): 35,
    ("Camiseta", "G"): 40,
    ("Calça", "M"): 30,
    ("Calça", "G"): 35
}

produto = input("Digite o produto: ")
tamanho = input("Digite o tamanho: ").upper()

valor = "" 

for (p, t), v in precos.items():
    if produto == p and tamanho == t:
        valor = v 

if valor:
    print(f"O valor é {valor}")
else:
    print("Produto ou tamanho não encontrado.")
