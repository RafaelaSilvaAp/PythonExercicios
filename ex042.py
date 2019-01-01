r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('é possível formar um triângulo')
    if r1 == r2 == r3:
        print('O Triângulo é Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O Triângulo é Isósceles')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('O Triângulo é Escaleno')
else:
    print('não é possível formar um triângulo')