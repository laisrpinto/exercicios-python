lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Resposta inválida. Quer continuar?')).strip().upper()[0]
    if resposta == 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
print('O valor 5 faz parte da lista.' if 5 in lista else 'O valor 5 não foi encontrado na lista.')