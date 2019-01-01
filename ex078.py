valores = []
maior = menor = 0
for i in range(0, 5):
    valores.append(int(input(f'Digite valor para posição {i}: ')))
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]

print('-'*30)
print(f'Os valores digitados são: {valores}')
print(f'O maior valor digitado foi {maior} na(s) posição(ões): ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()

print(f'O menor valor digitado foi {menor} na(s) posição(ões): ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()
