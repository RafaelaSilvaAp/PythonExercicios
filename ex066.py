n = c = s = 0

while True:
    n = int(input('Digite valor: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Soma = {s}')
print(f'Quantidade de valores digitados = {c}')