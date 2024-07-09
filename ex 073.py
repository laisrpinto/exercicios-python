times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense',
         'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá','Corinthians',
         'Cruzeiro', 'Vasco da Gama', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'Américo-MG')
print('='*15,'TABELA BRASILEIRÃO 2023', '='*15)
print(f'Lista com os times: {times}')
print('='*55)
print(f'Os 5 primeiros são {times[0:5]}')
print('='*55)
print(f'Os 4 últimos são {times[-4:]}')
print('='*55)
print(f'Times em ordem alfabética: {sorted(times)}')
print('='*55)
print(f'O internacional está na {times.index("Internacional") + 1}ª posição')
print('='*55)
while True:
    usuario = str(input('Digite um time para ver a sua posição: ')).strip().capitalize()
    if usuario not in times:
        print('Digitou o nome do time errado. Tente novamente')
    else:
        break
print('='*55)
print('O {} está na posição {}ª'.format(usuario, times.index(usuario) + 1))
