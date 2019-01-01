s = ''
while s != 'M' and s != 'F':
    s = str(input('Digite Sexo: ')).upper()
    if s != 'M' and s != 'F':
        print('Você digitou um valor inválido, Por favor digite novamente')
print('Você digitou um valor correto')