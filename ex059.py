n1 = int(input('Digite primeiro valor: '))
n2 = int(input('Digite segundo valor: '))

op = 0

while op != 5:
    op = int(input(''' Escolha
     [1] Somar
     [2] Multiplicar
     [3] Maior
     [4] Novos Números
     [5] Sair do Programa
     Sua Opção: '''))
    if op == 1:
        print('O resultado de {} + {} = {}'.format(n1, n2, n1 + n2))
    if op == 2:
        print('O resultado de {} x {} = {}'.format(n1, n2, n1 * n2))
    if op == 3:
        if n1 > n2:
            print('O {} é maior que {}'.format(n1, n2))
        else:
            print('O {} é maior que {}'.format(n2, n1))
    if op == 4:
        n1 = int(input('Digite primeiro valor: '))
        n2 = int(input('Digite segundo valor: '))
    if op > 5:
        print('Opção Inválida! Tente Novamente.')

print('Finalizando Programa...')
