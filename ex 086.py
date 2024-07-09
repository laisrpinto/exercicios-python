'''matriz = [[[ ], [ ], [ ]], [[ ], [ ], [ ]], [[ ], [ ], [ ]]]
for c in range(0,9):
    if 0 <= c < 3:
        num = int(input(f'Digite um valor para a posição [{0, c}]: '))
        matriz[0][c].append(num)
    elif 3 <= c < 6:
        num = int(input(f'Digite um valor para a posição [{1, c - 3}]: '))
        matriz[1][c - 3].append(num)
    elif 6 <= c < 9:
        num = int(input(f'Digite um valor para a posição [{2, c - 6}]: '))
        matriz[2][c - 6].append(num)
for l in range(0,3):
    print(f'{matriz[0][l]}', end= '')
for p in range(0,4):
    print('\n' if p == 0 else f'{matriz[1][p-1]}', end= '')
for m in range(0,4):
    print('\n' if m == 0 else f'{matriz[2][m-1]}', end='')'''

#SOLUÇÃO GUANABARA:
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        num = 9
        matriz[l][c] = int(input(f'Digite um valor para [{l,c}]: '))
print('='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
