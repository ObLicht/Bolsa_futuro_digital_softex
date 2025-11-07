from models.cliente import Cliente
from models.produto import Produto
from dao.cliente_dao import ClienteDAO
from dao.produto_dao import ProdutoDAO

def menu():
    opcoes = ["Cadastrar Cliente", "Cadastrar Produto", "Listar Clientes", "Listar Produtos","Listar Clientes e Produtos", "Sair"]
    for i, opcao in enumerate(opcoes):
        print(f"{i} - {opcao}")

dao_clientes = ClienteDAO()

dao_produtos = ProdutoDAO()



while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "0":
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")

        cliente = Cliente(nome, email, telefone)
        dao_clientes.salvar(cliente)
        print("✅ Cliente cadastrado!")
    
    elif opcao =="1":
        item = input("Produto: ")
        produto = Produto(item)
        dao_produtos.salvar(produto)
        print("✅ Produto cadastrado!")


    elif opcao == "2":
        clientes = dao_clientes.listar()
        for c in clientes:
            print(c)

    elif opcao == "3":
        produtos = dao_produtos.listar()
        for p in produtos:
            print(p)

    elif opcao == "4":
        clientes = dao_clientes.listar()
        for c in clientes:
            print(c)
        produtos = dao_produtos.listar()
        for p in produtos:
            print(p)

    elif opcao == "5":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")