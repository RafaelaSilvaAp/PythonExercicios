n = int(input('Digite um número: '))
c = 0
for i in range (1, n+1):
    if n % i == 0:
        c = c + 1
print('O número foi dividido {} vezes'.format(c))
if c == 2:
    print('O número PRIMO')
else:
    print('O número Não é PRIMO')