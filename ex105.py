def notas(* notas, situacao=False):
    """
    Função que recebe várias notas e retorna dados como a
    quantidade, maior, menor e média das notas
    :param notas:  Valores numéricos equivalentes as notas dos alunos
    :param situacao: Situação da Turma (opcional)
    :return: Ficha com as informações da turma
    """
    maior = menor = media = 0
    quantidade = len(notas)
    ficha = dict()

    for c, v in enumerate(notas):
        media += v
        if c == 0:
            maior = v
            menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v

    media = media / quantidade
    ficha['quantidade'] = quantidade
    ficha['maior'] = maior
    ficha['menor'] = menor
    ficha['media'] = media

    if situacao == True:
        if media < 5:
            ficha['situacao'] = 'RUIM'
        elif 5 >= media < 7:
            ficha['situacao'] = 'REGULAR'
        elif media >= 7:
            ficha['situacao'] = 'BOA'

    return ficha


n = notas(5, 9, 8, 6, 7, situacao=True)
print(n)


help(notas)