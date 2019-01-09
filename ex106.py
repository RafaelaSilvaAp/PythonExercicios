from time import sleep

def pyHelp():
    while True:
        print('--' * 20,f'\n        SISTEMA DE AJUDA PyHelp', flush=True)
        print('--' * 20)
        sleep(0.5)
        comando = str(input('\nFunção ou Biblioteca > '))
        print()
        if comando == 'fim':
            print('--' * 20, '\n               ATÉ LOGO')
            print('--' * 20)
            break
        print()
        sleep(0.5)
        print('--' * 20, f'\n  Acessando o manual do comando {comando}')
        print('--' * 20)
        print()
        sleep(1)
        print(help(comando))


pyHelp()