def alterar_idade(nome_usuario, idade_usuario):
    if nome_usuario in pessoas:
        pessoas[nome_usuario] = idade_usuario
    else:
        print("Pessoa não encontrada!")


pessoas = {
    "ana": 22,
    "arthur": 15,
    "carlos": 3
}

nome_usuario = input("Digite o nome: ").lower()

try:
    idade_usuario = int(input("Digite a nova idade: "))

    if 0 <= idade_usuario <= 116: #A pessoa mais velha do mundo atualmente tem 116 anos, segundo o Google.
        alterar_idade(nome_usuario, idade_usuario)

except:
    print("Idade inválida")
    
print(pessoas)
