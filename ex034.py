sal = float(input('Informe o salário: '))
if sal > 1250:
    sal = sal + (sal * 0.1)
    print('O novo salário é R$ {}'.format(sal))
if sal <= 1250:
    sal = sal + (sal * 0.15)
    print('O novo salário é R$ {}'.format(sal))
