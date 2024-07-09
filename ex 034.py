sal = float(input('Informe seu salário atual: '))

if sal>1250:
    aum1 = sal + (sal * 0.1)
    print('Você receberá um aumento de 10%. Seu sálario será R${}.'.format(aum1))
else:
    aum2 = sal + (sal * 0.15)
    print('Você receberá um aumento de 15%. Seu salário será R${}.'.format(aum2))
