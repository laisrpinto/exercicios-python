#VER SOLUÇÃO DO GUANABARA

num = int(input('Digite um número: '))
soma = menor = maior = num
contador = 1
continuação = str(input('Quer continuar? [S/N] ')).strip().upper()
while continuação == 'S':
    num = int(input('Digite um número: '))
    continuação = str(input('Quer continuar? [S/N] ')).strip().upper()
    soma += num
    contador += 1
    if maior < num:
        maior = num
    elif menor > num:
        menor = num
media = soma /contador
print('Você digitou {} números e a média entre eles foi {}'.format(contador, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))