import datetime
atual = datetime.date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu ? '.format(i)))
    idade = atual - nasc
    if idade >= 21:
        #print('Essa pessoa é maior')
        totmaior += 1
    else:
        #print('Essa pessoa é menor')
        totmenor += 1
print('{} pessoas são maiores de idade'.format(totmaior))
print('{} pessoas são menores de idade'.format(totmenor))