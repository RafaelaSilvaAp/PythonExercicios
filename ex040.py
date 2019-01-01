n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
m = (n1 + n2)/2
print('A média do Aluno é = {}'.format(m))
if m < 5:
    print('O aluno está reprovado!')
elif 7 > m >= 5:
    print('O aluno está de recuperação!')
elif m >= 7:
    print('O aluno está aprovado!')
