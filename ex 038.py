'''n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
if n1 > n2:
    print('O primeiro número é maior.')
elif n2 > n1:
    print('O segundo número é maior.')
else:
    print('Os dois valores são iguais.')'''

n = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número: '))
maior = n

if n < n2:
    maior = n2
    print('n2 é maior')
elif n == n2:
    print('os valore sao iguais')