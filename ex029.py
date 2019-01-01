vel = float(input('Qual a velocidade do carro: '))
if vel > 80:
    print('Você excedeu a velocidade!')
    mul = (vel - 80) * 7
    print('Terá que pagar de multa R$ {:.2f}'.format(mul))
else:
    print('Está dentro do limite!')