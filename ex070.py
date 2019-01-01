total = barato = c = i = 0
nome_barato = ''
while True:
    produto = str(input('Produto: '))
    valor = float(input('Valor: R$ '))
    i += 1
    if i == 1:
        barato = valor
    else:
        if valor < barato:
            barato = valor
            nome_barato = produto
            print(f'{nome_barato}')
    total += valor
    if valor > 1000:
        c += 1

    op = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if op in 'Nn':
        break

print(f'Total da compra = R$ {total}')
print(f'Quantidade de valores acima de R$ 1000,00 = {c}')
print(f'Produto mais barato custou R$ {barato} e é {nome_barato}')

