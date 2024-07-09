from datetime import date
ano = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano

if ano < 1900 or ano > anoatual:
    print("O ano que você digitou é inválido")
elif idade <= 9:
    print(f'Você tem {idade} anos. Sua categoria é', end=' ')
    print('MIRIM')
elif idade <= 14:
    print(f'Você tem {idade} anos. Sua categoria é', end=' ')
    print('INFANTIL')
elif idade <= 19:
    print(f'Você tem {idade} anos. Sua categoria é', end=' ')
    print('JUNIOR')
elif idade <= 25:
    print(f'Você tem {idade} anos. Sua categoria é', end=' ')
    print('SENIOR')
elif idade > 25:
    print(f'Você tem {idade} anos. Sua categoria é', end=' ')
    print('MASTER')

