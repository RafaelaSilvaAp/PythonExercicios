n = 0
soma = 0
cont = 0
print('Digite qualquer valor. Digite 999 para parar')
n = int(input('Valor: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Valor: '))
print('Acabou')
print('Você digitou {} números. A soma é = {}'.format(cont, soma))