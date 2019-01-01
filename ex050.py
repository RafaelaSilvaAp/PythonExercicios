s = 0
for i in range (1, 7):
    n = int(input('Digite {}º Valor: '.format(i)))
    if n % 2 == 0:
        s += n
print('O somatório dos pares é = {}'.format(s))
