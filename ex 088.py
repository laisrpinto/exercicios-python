from random import randint
from time import sleep
print('-'*50)
print(f'{"JOGO NA MEGA SENA":^50}')
print('-'*50)
jogos = int(input('Quantos jogos você quer sortear? '))
print('-'*15,f'Sorteando {jogos} jogos','-'*15)
contar = 0
lista_jogos = []
dados = []
for c in range(0, jogos):
    for p in range(0, 6): #tentei com o while primeiro e não deu
        dados.append(randint(1,60))
        contar += 1
    lista_jogos.append(dados[:])
    dados.clear()
    print(f'Jogo {c+1}: {lista_jogos[c]}')
    sleep(1)
print('-'*20, 'BOA SORTE', '-'*19)




