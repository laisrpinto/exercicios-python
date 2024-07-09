somaidade = 0
velhoi = 0
velhon = ''
mulheres = 0
for c in range (1,5):
    print('-'*5, '{} PESSOA'.format(c), '-'*5)
    nome = str(input('Nome: ')).upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).upper()
    somaidade += idade
    if c == 1 and sexo == 'M':
        velhoi = idade
        velhon = nome
    elif idade > velhoi and sexo == 'M':
        velhoi = idade
        velhon = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1
media = somaidade/c
print('A média da idade do grupo é {:.2f}.'.format(media))
print('O homem mais velho é {} e sua idade é {}.'.format(velhon, velhoi))
if mulheres == 1:
    print('Tem apenas 1 mulher com menos de 20 anos.')
elif mulheres > 1:
    print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres))
