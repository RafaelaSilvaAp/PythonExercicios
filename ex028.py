import random

rand = random.randint(0 , 5)
num = int(input('Tente adivinhar em qual número o PC está pensando, de 0 a 5: '))
if num == rand:
    print('Você Acertou, Parabéns! O número era {}'.format(rand))
else:
    print('Que pena, você errou!, o número era {}'.format(rand))