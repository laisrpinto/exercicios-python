from time import sleep


def maior(* num):
    maior = 0
    print('=' * 50)
    print('Analisando os valores passados...')
    for c in num:
        print(c, end=' ')
        sleep(0.3)
        if c > maior:
            maior = c
    print(f'Foram informandos {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa Principal
maior(1, 7, 4, 5, 9, 12)
maior(14, 20, 1)
maior(9, 7)
maior(7)
maior()