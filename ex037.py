n = int(input('Digite um número inteiro: '))
op = int(input('Escolha uma base para conversão: \n[1] Binário\n[2] Octal\n[3] Hexadecimal\nSua opção: '))

if op == 1:
    print('{} Convertido para binário é = {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('{} Convertido para octal é = {}'.format(n, oct(n))[2:])
elif op == 3:
    print('{} Convertido para hexadecimal é = {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida!')
