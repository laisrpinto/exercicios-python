galera = []
dado = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    galera.append(dado[:])
    dado.clear()
    for p in range(0, len(galera)):
        if p == 0:
            maior = menor = galera[p][1]
        else:
            if maior < galera[p][1]:
                maior = galera[p][1]
            if menor > galera[p][1]:
                menor = galera[p][1]
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('Resposta inválida.')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Ao todo você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {maior}. Peso de ', end= '')
for c in galera:
    if c[1] == maior:
        print(f'{c[0]}', end=' ')
print(f'\nO menor peso foi de {menor}. Peso de ', end=' ')
for c in galera:
    if c[1] == menor:
        print(c[0], end=' ')



