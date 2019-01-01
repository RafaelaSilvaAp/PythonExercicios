ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('--' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('--' * 20)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('--' * 30)
    op = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if op == 999:
        break
    if op <= len(ficha) - 1:
        print(f'Notas de {ficha[op][0]} são {ficha[op][1]}')
print('<<< FIM DA EXECUÇÃO >>>')
