alunos = {
    ("luis", "Matemática"): 9,
    ("luis", "História"): 7,
    ("ana", "Inglês"): 5,
    ("ana", "Português"): 2
}

nome_aluno = input("Qual o nome do aluno: ").lower()

total = 0
contador = 0

for (nome, materia), nota in alunos.items():
    if nome == nome_aluno:
        print(f"{materia}: {nota}")
        total += nota
        contador += 1

if contador > 0:
    media = total / contador
    print(f"Média geral: {media:.2f}")
else:
    print("Aluno não encontrado.")
