matriz = [[[], [], []], [[], [], []], [[], [], []]]
pares = terceira = maior = 0
for c in range(0,9):
    if 0 <= c < 3:
        matriz[0][c].append(int(input(f'Digite um valor para a posição [{0, c}]: ')))
    elif 3 <= c < 6:
        matriz[1][c - 3].append(int(input(f'Digite um valor para a posição [{1, c - 3}]: ')))
    elif 6 <= c < 9:
        matriz[2][c - 6].append(int(input(f'Digite um valor para a posição [{2, c - 6}]: ')))
for p in range(0,9):
    if 0 <= p < 3:
        print(matriz[0][p], end='')
        if matriz[0][p][0] % 2 == 0:
            pares += matriz[0][p][0]
    elif 3 <= p < 6:
        print(f'\n{matriz[1][0]}' if p == 3 else matriz[1][p - 3], end='')
        if matriz[1][p-3][0] % 2 == 0:
            pares += matriz[1][p-3][0]
        if p == 3:
            maior = matriz[1][0][0]
        else:
            if maior < matriz[1][p-3][0]:
                maior = matriz[1][p-3][0]
    elif 6 <= p < 9:
        print(f'\n{matriz[2][0]}' if p == 6 else matriz[2][p - 6], end='')
        if matriz[2][p-6][0] % 2 == 0:
            pares += matriz[2][p-6][0]
        terceira += matriz[2][p-6][0]
print(f'\n{"="*50}')
print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {terceira}')
print(f'O maior valor da segunda linha é: {maior}')
print('='*50)
