dist = float(input('Qual é a distância da viagem? '))
if dist <= 200:
    custo = dist * 0.5
    print('A viagem vai custar R$ {:.2f}'.format(custo))
else:
    custo = dist * 0.45
    print('A viagem vai custar R$ {:.2f}'.format(custo))
