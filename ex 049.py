n = int(input('Digite um número para ver sua tabuada: '))
print('='*20)
for c in range(1,11):
    tabuada = n * c
    print('{} X {} = {}'.format(n, c, tabuada))
print('='*20)