alunos = []
nomes = []
notas = []
while True:
    nomes.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    nomes.append(notas[:])
    nomes.append((notas[0] + notas[1]) / 2)
    alunos.append(nomes[:])
    nomes.clear()
    notas.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('Resposta inválida.')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-'*50)
print(f'{"Nº":<7}', end='')
print(f'{"Nome":<7}', end='')
print(f'{"Média":<7}')
print('-'*50)
for c in range(0, len(alunos)):
    print(f'{c:<7}', end='')
    print(f'{alunos[c][0]:<7}', end='')
    print(f'{alunos[c][2]:<7}')
    if c == len(alunos):
        print(end='')





