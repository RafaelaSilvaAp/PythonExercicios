def escreva(msg):
    print('-' * (len(msg) + 2))
    print(f' {msg:^} ')
    print('-' * (len(msg) + 2))


msg = str(input('Digite uma palavra ou frase: '))
escreva(msg)

