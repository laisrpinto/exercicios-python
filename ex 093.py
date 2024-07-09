jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = list()
tot = 0
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    tot += gols[c]
jogador['gols'] = gols[:] #Não esquecer de fazer a cópia
jogador['total'] = tot #Alternativa: jogador['total'] = sum(gols), não preciso fazer o acumulador
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f' -O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for c, v in enumerate(gols):
    print(f'  => Na partida {c}, fez {v} gols.')
print(f'Foi um total de {tot} gols.')