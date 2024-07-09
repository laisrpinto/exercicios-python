r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 >r1:
    print('Suas medidas são {}, {} e {}. Sendo assim é possível formar um triangulo.'.format(r1,r2,r3))
else:
    print('Suas medidas são {}, {} e {}. Não é possível formar um triangulo.'.format(r1,r2,r3))