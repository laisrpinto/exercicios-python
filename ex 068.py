from random import randint
print('-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('-'*30)
contador = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    soma = jogador + computador
    jogada = ' ' #Se não coloco um espaço aqui, o programa não vai pra frente. Por que?
    while jogada not in 'PI':
        jogada = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print('-'*30)
    print(f'Você jogou {jogador} e computador {computador}. A soma total foi {soma}.', 'Deu PAR' if soma % 2 == 0 else 'Deu ÍMPAR')
    print('-' * 30)
    if jogada == 'P' and soma % 2 == 00:
        print('VOCÊ VENCEU!!!')
        print('Vamos jogar novamente...')
    elif jogada == 'I' and soma % 2 != 0:
        print('VOCÊ VENCEU!!!')
        print('Vamos jogar novamente...')
    else:
        print('Você perdeu!')
        print('-' * 30)
        break
    contador += 1
print(f'GAME OVER. Você venceu {contador} vezes.')


