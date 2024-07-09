listanum = []
while True:
    num = int(input('Digite um valor: '))
    if num in listanum:
        print('Valor duplicado. Não vou adicionar.')
    else:
        listanum.append(num)
        print('Valor adicionado com sucesso.')
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        print('Resposta inválida. Digite S ou N.')
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('='*40)
print(f'Você digitou os valores {sorted(listanum)}')
