r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
print(f'Suas medidas são {r1}, {r2} e {r3}.')

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Condição para formar um triângulho satisfeita!')
    if r1 == r2 == r3:
        print('Suas medidas formam um triângulo EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Suas medidas formam um triângulo ISÓSCELES.')
    elif r1 != r2 != r3 != r1:
        print('Suas medidas formam um triângulo ESCALENO.')
else:
    print('Não é possível formar um triângulo')
