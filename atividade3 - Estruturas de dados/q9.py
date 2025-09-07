alunos = {
    ("Ana", "Matemática") : (9.1, 4.5, 7.0),
    ("Carlos", "Matemática") : (3.5, 4.4, 8.9),
    ("Carol", "Matemática") : (9.8, 8.6, 5.6),
    ("Pedro", "Matemática") : (10.0, 7.7, 8.5)
}

def calcular_media(notas):
    return sum(notas) / len(notas)

def cadastrar_aluno(nome, disciplina, notas):
    alunos[(nome, disciplina)] = notas
    print(f"Aluno {nome} cadastrado.")

def consultar_notas(nome):
    for (aluno_nome, disciplina), notas in alunos.items():
        if aluno_nome == nome:
            media = calcular_media(notas)
            print(f"Para {disciplina} -> Notas: {notas}; Média: {media:.2f}")

cadastrar_aluno("Arthur", "Matemática", (8.0, 9.5, 7.5))
consultar_notas("Arthur")
consultar_notas("Ana")
