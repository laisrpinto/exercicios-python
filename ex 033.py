a = int(input('Primeiro número '))
b = int(input('Segundo número '))
c = int(input('Terceiro número '))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {} e o maior valor digitado foi {}.'.format(menor, maior))
