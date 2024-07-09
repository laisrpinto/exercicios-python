time = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0,partidas):
        gols.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
while True:
    indice = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if indice >= len(time):
        print(f'ERRO! Não existe jogador com código{indice}!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[indice]["nome"]}:')
        for c, v in enumerate(time[indice]['gols']):
            print(f'  => Na partida {c+1}, fez {v} gols.')
    print('-='*30)
    if indice == 999:
        break
