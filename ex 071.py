'''print('='*40)
print('{:^40}'.format('BANCO CEV'))
print('='*40)
valor = int(input('Qual valor você quer sacar? R$'))
inteiro50 = inteiro20 = inteiro10 = inteiro1 = 0
while True:
    if valor / 50 >= 1:
        inteiro50 = int(valor / 50)
        valor = valor - inteiro50 * 50
    if valor / 20 >= 1:
        inteiro20 = int(valor / 20)
        valor = valor - inteiro20 * 20
    if valor / 10 >= 1:
        inteiro10 = int(valor / 10)
        valor = valor - inteiro10 * 10
    if valor / 10 < 1:
        inteiro1 = valor
        valor = valor - inteiro1
    if valor == 0:
        break
if inteiro50 >= 1:
    print(f'Total de {inteiro50} cédulas de R$50')
if inteiro20 >= 1:
    print(f'Total de {inteiro20} cédulas de R$20')
if inteiro10 >= 1:
    print(f'Total de {inteiro10} cédulas de R$10')
if inteiro1 >= 1:
    print(f'Total de {inteiro1} cédulas de R$1')
print('='*40)
print('Obrigada por escolher o BANCO CEV.')'''

#SOLUÇÃO GUANABARA:
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total = total - céd
        totcéd = totcéd + 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('FIM')