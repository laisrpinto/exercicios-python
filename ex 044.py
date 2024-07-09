print('{:-^40}'.format(' LOJAS RAJARAM '))
preço = float(input('Qual foi o valor das suas compras? '))
print('''OPÇÕES DE PAGAMENTO:
[1] À VISTA EM DINHEIRO
[2] À VISTA EM CARTÃO
[3] 2X NO CARTÃO
[4] DE 3X A 10X NO CARTÃO''')
opção = int(input('Escolha uma forma de pagamento: '))
if opção < 1 or opção > 4:
    print('Opção inválida. Digite um número entre 1 e 4.')
elif opção == 1:
    pagamento = preço - (preço * (10/100))
    print('Escolheu a opção À VISTA EM DINHEIRO e por isso irá receber 10% de desconto. \n'
          'O valor total a pagar é {:.2f}R$'.format(pagamento))
elif opção == 2:
    pagamento = preço - (preço * (5/100))
    print('Escolheu a opção À VISTA EM CARTÃO e por isso rá receber 5% de desconto. \n'
          'O valor total a pagar será de {:.2f}R$'.format(pagamento))
elif opção == 3:
    print('Escolheu a opção 2X NO CARTÃO. O valor total a pagar é {}R$'.format(preço))
elif opção == 4:
    parcela = int(input('Em quantas parcelas irá pagar? '))
    if parcela < 3 or parcela > 10:
        print('Número de parcelas inválido para essa opção.')
    else:
        pagamento = preço + (preço * (20/100))
        print('Escolheu a opção 3X A 10X NO CARTÃO.Tem um acréscimo de 20% de juros.\n'
              'O valor total a pagar será de {}'.format(pagamento))
