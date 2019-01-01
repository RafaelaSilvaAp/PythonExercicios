alunos = dict()
alunos['nome'] = str(input('Nome do Aluno: '))
alunos['media'] = float(input('Média do Aluno: '))
print(f'O nome do Aluno é {alunos["nome"]}')
print(f'A média do Aluno é {alunos["media"]}')

if alunos['media'] >= 7:
    alunos['situacao'] = 'Aprovado'
elif alunos['media'] >= 5 and alunos['media'] < 7:
    alunos['situacao'] = 'Recuperação'
else:
    alunos['situacao'] = 'Reprovado'
print(f'A situação do {alunos["nome"]} é {alunos["situacao"]}')