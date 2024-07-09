num = int(input('Digite um número para ver se ele é primo: '))
contar = 0
for c in range(1, num + 1):
    if num % c == 0:
        contar += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
if contar == 2:
    print(' \n \33[mé primo')
else:
    print('\n \33[mnão é primo')
