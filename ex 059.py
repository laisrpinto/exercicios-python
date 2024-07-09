from time import sleep
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('=' * 25)
    print('''[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    print('=' * 25)
    if opção == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} é {}'.format(valor1, valor2, soma))
    if opção == 2:
        multi = valor1 * valor2
        print('A multiplicação entre {} e {} é {}'.format(valor1, valor2, multi))
    if opção == 3:
        if valor2 > valor1:
            print('O maior valor digitado foi {}'.format(valor2))
        elif valor1 > valor2:
            print('O maior valor digitado foi {}'.format(valor1))
        elif valor1 == valor2:
            print('Os valores são iguais.')
    if opção == 4:
        print('Informe os números novamente.')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input(('Segundo valor: ')))
    if opção > 5:
        print('Opção inválida. Tente novamente.')
print('Finalizando...')
sleep(3)
print('Fim do programa. Volte sempre!')