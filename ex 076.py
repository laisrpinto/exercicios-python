print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}') #^ SIGNIFICA CENTRALIZAR
print('-'*40)
produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='') #< SIGNIFICA: ALINHAR A ESQUERDA, E > SIGNIFICA ALINHAR A DIREITA
    else:
        print(f'R$ {produtos[c]:>7.2f}')
print('-'*40)




