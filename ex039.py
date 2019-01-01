from datetime import date

atual = date.today().year
nasc = int(input('Data de Nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} para o alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(atual + saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já devia ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(atual - saldo))