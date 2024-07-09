print('='*15, 'PROGRESSÃO ARITMÉTICA', '='*15)
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
termo = primeiro
contador = 1
print('Os 10 termos da progessão são: ', end='')
while contador <= 10:
    print('{} ->'.format(termo), end=' ')
    termo += razão
    contador += 1
print('FIM')
