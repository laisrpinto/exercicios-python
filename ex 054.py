from datetime import date
menor = 0
maior = 0
for ano in range (1, 8):
    nascimento = int(input('Em que ano a {}ª pesssoa nasceu: '.format(ano)))
    idade = date.today().year - nascimento
    if nascimento < 1900 or nascimento > date.today().year:
        print('digitou algum ano inválido. Tente novamente')
    elif idade >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo temos {} pessoas maiores de idade e {} menores de idade.'.format(maior, menor))
