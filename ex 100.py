from random import randint
from time import sleep
numeros = list()


def sorteia(lista):
    print('Sorteando 5 valores: ', end=' ')
    cont = 0
    while cont < 5:
        numeros.append(randint(1, 10))
        print(lista[cont], end=' ')
        sleep(0.3)
        cont += 1
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma} ')


sorteia(numeros)
somaPar(numeros)
