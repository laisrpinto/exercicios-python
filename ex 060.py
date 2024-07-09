'''num = int(input('Digite um número para calcular seu fatorial: '))
acumula = 1
print('Calculando {}! = '.format(num), end='')
while num > 0:
    if num > 1:
        print('{} x '.format(num), end='')
    else:
        print('{} ='.format(num), end=' ')
    acumula = acumula * num
    num = num - 1
print(acumula)'''

#FAZENDO COM O FOR:
num = int(input('Digite um número para calcular seu fatorial: '))
acumula = 1
for c in range(num, 0, -1):
    print('{} '.format(c), end='')
    print(' x ' if c != 1 else '=', end=' ')
    acumula *= num
    num -= 1
print(acumula)