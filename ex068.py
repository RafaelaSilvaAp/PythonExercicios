import random
c = 0
while True:
    pc = random.randint(1, 10)
    n = int(input('Escolha um número: '))
    op = str(input('Escolha Par ou Impar [P/I]: ')).strip().upper()
    s = pc + n
    if s % 2 == 0 and op in 'Pp' or s % 2 != 0 and op in 'Ii':
        c += 1
        print(f'Você ganhou essa rodada!\nO computador escolheu {pc}')

    if s % 2 != 0 and op in 'Pp' or s % 2 == 0 and op in 'Ii':
        print(f'Você perdeu! \nVocê teve {c} vitória(s)')
        break
print('Jogo Finalizado!')



