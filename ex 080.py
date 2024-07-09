listanum = []
'''maior = menor = 0
for c in range(0,5):
    num = int(input('Digite um valor: '))
    if c == 0:
        maior = menor = num
    if maior <= num:
        listanum.insert(4, num)
        maior = num
        print('Valor dicionado ao final da lista.')
    elif menor >= num:
        listanum.insert(0,num)
        menor = num
        print(f'Valor adicionado na posição 0 da lista.')
    elif menor < num < maior:
        listanum.insert(1, num)
        print(f'Valor adicionado na posição {1} da lista')
    elif num > listanum[1]:
        listanum.insert(2, num)
        print('Valor adicionado na posição 2 da lista')
print(listanum)
max(listanum)'''

#SOLUÇÃO GUANABARA:
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0 or n >= listanum[-1]:
        listanum.append(n)
    else:
        pos = 0
        while pos < len(listanum):
            if n <= listanum[pos]:
                listanum.insert(pos,n)
                break
            pos += 1
print(listanum)