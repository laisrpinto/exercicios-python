nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
print(f'A média entre {nota1} e {nota2} é {media}')
if media >= 7:
    print('Você foi aprovado!')
elif 5<= media <=6.9:
    print('Você está em recuperação.')
elif media < 5:
    print('Você foi reprovado.')