'''lista_completa = []
lista_pares = []
lista_impares = []
while True:
    n = int(input('Digite um número: '))
    lista_completa.append(n)
    lista_pares.append(n) if n % 2 == 0 else lista_impares.append(n)
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        print('Resposta inválida. Digite S ou N.')
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'A lista completa é {lista_completa}')
print(f'A lista dos números pares é {lista_pares}')
print(f'A lista dos números ímpares é {lista_impares}')'''

#outra solução:

lista_completa = []
pares = []
impares = []
while True:
    lista_completa.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
for c, i in enumerate(lista_completa):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(lista_completa)
print(pares)
print(impares)