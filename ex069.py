m18 = qh = mul = 0
while True:
    idade = int(input('Digite idade: '))
    sexo = str(input('Digite sexo [F/M]:')).upper().strip()
    if idade > 18:
        m18 += 1
    if sexo in 'Mm':
        qh += 1
    if sexo in 'Ff' and idade < 20:
        mul += 1
    op = str(input('Deseja continuar [S/N] ? '))
    if op in 'Nn':
        break
print(f'Quantidade de pessoas com mais de 18 anos: {m18}')
print(f'Quantidade de homens cadastrados: {qh}')
print(f'Quantidade de mulheres com menos de 20 anos: {mul}')