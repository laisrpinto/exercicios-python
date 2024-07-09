'''print('='*10, 'PROGRESSÃO ARITMÉTICA MELHORADA', '='*10)
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
termo = primeiro
contador_inicial = 1
mais_termos = 1
total_termos = 10
while mais_termos != 0:
    while contador_inicial <= 10:
        print('{} -> '.format(termo), end='')
        termo += razão
        contador_inicial += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos você quer mostrar mais? '))
    for c in range(contador_inicial, contador_inicial + mais_termos):
        print('{} ->'.format(termo), end=' ')
        termo += razão
    total_termos += mais_termos
print('Progressão finalizada com {} termos mostrados'.format(total_termos))'''

#SOLUÇÃO DO GUANABARA:

print('='*10, 'PROGRESSÃO ARITMÉTICA MELHORADA', '='*10)
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        contador += 1
    print('PAUSA')
    mais  = int(input('Quantos termos você quer mostrar mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))