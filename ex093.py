jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input('Quantas partidas jogou ? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c} ? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('--' * 30)
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('--' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partida(s)')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
