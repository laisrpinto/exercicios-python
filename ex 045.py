from random import randint
from time import sleep
print('{:-^50}'.format(' VAMOS JOGAR JOKENPÔ? '))
jogador = int(input('''ESCOLHA UMA OPÇÃO:
[0] PEDRA
[1] PAPEL
[2] TESOURA
QUAL É A SUA JOGADA? '''))
computador = randint(0,2)
itens = ('Pedra', 'Papel', 'Tesoura')
if 0 <= jogador <= 2:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!!!')
    print('=' * 20)
    print('''Você escolheu {} \nComputador escolheu {}'''.format(itens[jogador], itens[computador]))
    print('=' * 20)
    if jogador == 0 and computador == 2 or jogador == 2 and computador == 1 or jogador == 1 and computador == 0:
        print('PARABÉNS. VOCÊ VENCEU!')
    elif jogador == computador:
        print('O jogo ficou empatado.')
    else:
        print('Que pena. Você não ganhou. ')
    #Não preciso escrever a condição de quando o computador ganha,
    #pq qualquer coisa diferente do empate ou de eu ganhar já é o computador ganhando.
    #Por isso o else basta
else:
    print('Opção inválida. Jogue novamente e se atende às opções corretas.')





