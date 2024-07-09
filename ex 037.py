'''n = int(input('Digite um número inteiro: '))
base = int(input('Escolha uma das bases para conversão: \n [1] BINÁRIA \n [2] OCTAL \n [3] HEXADECIMAL \n Sua opção: '))
if base == 1:
    print(f'{n} em base binária é {bin(n) [2:]}')
elif base == 2:
    print(f'{n} em base octal é {oct(n) [2:]}')
elif base == 3:
    print(f'{n} em base hexadecimal é {hex(n) [2:]}')
else:
    print('Opção inválida. Tente novamente.')'''

num = int(input('Digite um número inteiro em decimal: '))
print('''Escolha uma das seguintes opções de conversão:
[1] BINÁRIO
[2] HEXADECIMAL
[3] OCTAL''')
opção = int(input('Sua opção: '))

if opção == 1:
    print(f'O número {num} convertido para BINÁRIO é {bin(num)[2:]}.')
elif opção == 2:
    print(f'O número {num} convertido para HEXADECIMAL é {hex(num)[2:]}.')
elif opção == 3:
    print(f'O número {num} convertido para OCTAL é {oct(num)[2:]}.')
else:
    print('Opção inválidade. Escolha a opção 1 ou 2 ou 3.')