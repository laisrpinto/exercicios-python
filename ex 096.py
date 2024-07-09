def area(larg,compr):
    área = larg * compr
    print(f'A área de um terro {larg}x{compr} é {área}m².')


#Programa Principal
print(f' Controle de Terro')
print('-'* 25)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
