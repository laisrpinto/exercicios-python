'''casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12) #calculo para saber o valor da prestacao
minimo = salario * 0.30 #calculo para ver quanto é 30% do salario
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Seu empréstimo foi aprovado.')
else:
    print('Seu emprestimo não foi aprovado.', end='')
    print(' A prestação excede o minimo de {}'.format(minimo))'''

casa = float(input('Qual o valor da casa que você quer comprar? '))
salario = float(input("Quanto você recebe por mês? "))
anos = int(input('Em quantos anos você pretende pagar a casa? '))

mes = anos * 12
prestacao = casa / mes
trinta = salario * (30/100)

if prestacao <= trinta:
    print('PARABÉNS. Seu empréstimo foi aprovado. Sua prestação será de {} $'.format(prestacao))
else:
    print('Sua prestação de {} $ excede 30% do seu salario que é {} $. Por isso seu empréstimo foi negado'.format(prestacao, salario))

