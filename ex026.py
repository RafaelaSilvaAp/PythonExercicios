frase = str(input('Digite uma frase: ')).strip().upper()
print('A quantidade de vezes que a letra A aparece é {} vezes'.format(frase.count('A')))
print('A primeira letra a aparece na posição {}'.format(frase.find('A')))
print('A última letra A aparece na posição {}'.format(frase.rfind('A')))
