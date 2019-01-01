valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar ? [S/N]: '))
    if resp in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-' * 30)
print(f'Lista completa: {valores}')
print(f'Lista Pares: {pares}')
print(f'Lista Impares: {impares}')