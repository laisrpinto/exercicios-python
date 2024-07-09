'''lista = []
posicoes = []
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
maior = max(lista)
menor = min(lista)
for p in range(0,5):
    if lista[p] == maior:
        posicoes.append(p)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for p in range(0, len(posicoes)):
    print(str(posicoes[p]) + "...", end=' ')'''


#SOLUÇÃO GUANABARA:

listanum = []
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if maior < listanum[c]:
            maior = listanum[c]
        if menor > listanum[c]:
            menor = listanum[c]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i in range(0,5):
    if listanum[i] == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')

