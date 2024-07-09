print('-'*50)
print('{:^50}'.format('LOJA SUPER PREÇO'))
print('-'*50)
total = total1000 = contador = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço R$ '))
    contador += 1
    total += preço
    if preço > 1000:
        total1000 += 1
    if contador == 1 or preço < menor:   #NESSE CASO EU NÃO INICIEI A VARIÁVEL 'MENOR' LÁ EM CIMA E AINDA SIM DEU CERTO. PQ?
        menor = preço
        barato = produto
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if pergunta == 'N':
        break
print('-'*17, 'FIM DO PROGRMA', '-'*17)
print(f'O total da compra foi R${total}')
print(f'Temos {total1000} produtos custando mais de R$1.000,00.')
print(f'O produto mais barato foi {barato} custando R${menor}')