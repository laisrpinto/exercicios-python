from random import randint
valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
maior = menor = 0
for c in range(0,5):
    print(valores[c], end=' ')
    num = valores[c]
    if c == 0:
        maior = num
        menor = num
    elif maior < num:
        maior = num
    elif menor > num:
        menor = num
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')

#SOLUÇÃO GUANABARA:
print(f'O maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')

