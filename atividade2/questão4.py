def verificarSenha(senha):
    if len(senha) >= 8 and \
    any(c.islower() for c in senha) and \
    any(c.isupper() for c in senha) and \
    any(c.isdigit() for c in senha):
        print("Senha forte")
        
    else:
        print("Senha fraca")

senha = input(("Digite uma senha para verificação:"))

verificarSenha(senha)