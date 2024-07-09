from random import randint
print('Sou seu computador...\n'
      'Acabei de pensar em um número entre 0 e 10.\n'
      'Será que você consegue advinhar qual foi? ')
computador = randint(0,10)
usuario = int(input('Qual é seu palpite? '))
tentativas = 1
while computador != usuario:
    if usuario < computador:
        print('Mais... Tente mais uma vez.')
        usuario = int(input('Qual é o seu palpite? '))
    else:
        print('Menos... Tente mais uma vez.')
        usuario = int(input('Qual é o seu palpite? '))
    tentativas += 1
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))