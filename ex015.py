km = float(input('Informe quantidade de Km percorridos: '))
d = int(input('Informe quantidade de dias alugado: '))
c = (d * 60) + (km * 0.15)
print('O preço a ser pago é R$ {:.2f}'.format(c))
