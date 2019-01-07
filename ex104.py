def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
            print(f'Você digitou o valor numérico {n}')
        else:
            print('ERRO! Você digitou um valor não numérico')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')

