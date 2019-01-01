import random
num = rand = 100
c = 1
rand = random.randint(0 , 10)
# acertou = false while not acertou:
while rand != num:
    num = int(input('Tente adivinhar em qual número o PC está pensando, de 0 a 10: '))
    if num == rand:
        print('Você Acertou em {} tentativas, Parabéns!  O número era {}'.format(c, rand))
    else:
        print('Que pena, você errou! Tente Novamente')
        c += 1