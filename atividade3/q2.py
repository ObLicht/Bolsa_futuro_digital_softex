dados = {
    "Maria": ("(11) 9999-9999", "maria@email.com")
}

for nome, (telefone, email) in dados.items():
    print(f"{nome} → Telefone: {telefone} | Email: {email}")