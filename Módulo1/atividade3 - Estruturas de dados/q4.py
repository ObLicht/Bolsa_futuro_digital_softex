alunos = {
    "Luis": (8.6, 9.5, 7.4),
    "Junior": (7.0, 8.5, 9.0),
    "Caio": (6.5, 7.2, 8.0)
}

nome = input("Digite o nome do aluno: ")

if nome in alunos:
    notas = alunos[nome]
    print(f"Notas de {nome}: {notas}")
    media = sum(notas) / len(notas)
    print(f"Média de {nome}: {media:.2f}")
else:
    print("Aluno não encontrado!")

print("Médias de todos os alunos: ")
for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{aluno} → Notas: {notas} | Média: {media:.2f}")
