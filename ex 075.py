num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O número três não apareceu.')
print(f'Os valores pares digitados foram: ', end='')

'''if num[0] % 2 == 0:
    print(num[0], end=' ')
if num[1] % 2 == 0:
    print(num[1], end=' ')
if num[2] % 2 == 0:
    print(num[2], end=' ')
if num[3] % 2 == 0:
    print(num[3])'''

#SOLUÇÃO GUANABARA PROS NÚMEROS PARES:
for c in num:
    if c % 2 == 0:
        print(c, end=' ')



