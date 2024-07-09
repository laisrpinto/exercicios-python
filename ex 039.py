from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
if idade < 18:
    alis = 18 - idade
    if alis == 1:
        print(f'Ainda falta {alis} ano para o alistamento.')
        print(f'Seu alistamento será em {atual + alis}')
    else:
        print(f'Ainda faltam {alis} anos para o alistamento.')
        print(f'Seu alistamento será em {atual + alis}')
elif idade > 18:
    alis = idade - 18
    print(f'Você deveria ter se alistado há {alis}')
    print(f'Seu alistamento foi em {atual - alis}')
else:
    print('Você tem que se alistar imediatamente.')