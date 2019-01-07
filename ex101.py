def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')

    if idade < 16:
        return 'NEGADO'
    if idade >= 18 and idade <=65:
        return 'OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade > 65:
        return 'OPCIONAL'


ano = int(input('Digite seu ano de nascimento: '))
res = voto(ano)
print(res)
