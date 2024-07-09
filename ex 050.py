soma = 0
contar = 0
for num in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        contar += 1
print('Você foi informou {} números pares, a soma entre eles é {}'.format(contar, soma))