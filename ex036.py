casa = float(input('Qual é o valor da casa? R$ '))
sal = float(input('Quanto você ganha por mês? R$ '))
ano = int(input('Em quantos anos pretende pagar? '))

pres = casa / (ano * 12)
print('O valor de cada prestação é R$ {:.2f}'.format(pres))

if pres > (sal * 0.3):
    print('Infelizmente o empréstimo foi NEGADO.')
else:
    print('O empréstimo foi APROVADO.')