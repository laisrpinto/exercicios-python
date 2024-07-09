from random import shuffle
n1 = str(input('Primeiro Aluno '))
n2 = str(input('Segundo aluno '))
n3 = str(input('Terceiro Aluno '))
n4 = str(input('Quarto aAluno '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação é {}'.format(lista))