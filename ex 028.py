'''from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta advinhar
print('PROCESSANDO...')
sleep(3) #Pra dar três segundos antes de mostrar a resposta
if computador == jogador:
    print('PARABÉNS! Você venceu!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(computador, jogador))'''

from random import randint
from time import sleep
adivinha = int(input("Digite um número de 0 a 5: "))
num = randint(0,5)
print("Vamos ver se você ganhou...")
sleep(3)
if adivinha == num:
    print("VOCÊ GANHOU!!!")
else:
    print("O número que eu escolhi foi {}. Você não acertou".format(num))