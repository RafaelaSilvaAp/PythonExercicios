numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    valor = int(input('Digite um valor entre 0 e 20: '))
    if valor >= 0 and valor < 21:
        break
    else:
        print('Tente Novamente.')
print(f'Você digitou o número {numeros[valor]}')


