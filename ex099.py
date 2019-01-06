def maior(* num):
    cont = maior = 0
    print('\n Analisando os valores passados: ')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valor(es) ao todo')
    print(f'O maior valor encontrado foi {maior}')
    

maior(1, 5, 9, 25, 10, 2)
maior(5, -4, -7, 10)
maior(4)
maior()
