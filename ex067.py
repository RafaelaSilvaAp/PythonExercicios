n = m = 0
c = 1

while True:
    n = int(input('Quer ver a tabuada de qual valor ? '))
    if n < 0:
        break
    for c in range(1, 11):
        m = c * n
        print(f'{n} x {c} = {m}')
print('ACABOU!!!!')
