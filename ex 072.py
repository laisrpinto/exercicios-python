números = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
'''num = int(input('Digite um número para ve-lo escrito por extenso: '))
while num not in range(0,21):
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {números[num]}')'''

#SOLUÇÃO GUANABARA + SOLUÇÃO MINHA PARA O DESAFIO EXTRA:
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if  0 <= numero <= 20:
        print(f'Você digitou o número {números[numero]}')
        resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        while resposta not in 'SN':
            resposta = str(input('Resposta inválida. Quer continuar? [S/N]')).upper().strip()[0]
        if resposta == 'N':
            break
    else:
        print('Tente novamente.', end=' ')
