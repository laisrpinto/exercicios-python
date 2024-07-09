adultes = mulheres = homens = total = 0
while True:
    idade = int(input('Idade: '))
    sexo = pergunta = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if idade >= 18:
        adultes += 1
    if sexo == 'F' and idade < 20:      #O ELIF NÃO FUNCIONOU AQUI PQ PARA USAR O IF E O ELIF TENHO QUE COMPARAR VARIÁVEIS IGUAIS
        mulheres += 1
    elif sexo == 'M':
        homens += 1
    total += 1
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        print('Você interrompeu o cadastro')
        break
print(f'O total de pessoas cadastradas foram {total}')
print(f'{adultes} pessoas tem mais de 18 anos.')
print(f'Foram cadastradas {mulheres} mulheres com menos de 20 anos.')
print(f'O total de homens é {homens}')