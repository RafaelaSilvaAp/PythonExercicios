valor = float(input('Qual o valor total da compra ? R$ '))
print('Como você deseja efetuar o pagamento?'
      '\n[1] A vista (dinheiro/cheque)'
      '\n[2] A vista no cartão'
      '\n[3] 2x no cartão'
      '\n[4] 3x ou mais no cartão')
opcao = int(input('Qual sua opção ? '))

if opcao ==  1:
    saldo = valor - (valor * 0.1)
    print('O total de sua compra é {}'.format(saldo))
elif opcao == 2:
    saldo = valor - (valor * 0.05)
    print('O total de sua compra é {}'.format(saldo))
elif opcao == 3:
    print('O total de sua compra é {}, sendo duas parcelas de {}'.format(valor, valor/2))
elif opcao == 4:
    saldo = valor + (valor * 0.3)
    print('O total de sua compra é {}, sendo cada parcela no valor de R$ {}'.format(saldo, saldo/3))
else:
    print('Opção Inválida')
