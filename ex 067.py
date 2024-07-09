print('='*15,'TABUADA','='*15)
while True:
    n = int(input('Digite um número para ver a sua tabuada: '))
    print('='*45)
    if n < 0:
        break
    for c in range (1, 11):
        tabuada = c * n
        print(f'{n} x {c} = {tabuada}')
    print('='*45)
print('PROGRAMA ENCERRADO. VOLTE SEMPRE!')