
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: Fatorial de N
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)