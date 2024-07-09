from time import sleep
i = f = p = 0


def contador(i, f, p):
    print('=' * 40)
    print("Contagem de 1 até 10 de 1 em 1")
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.1)
    print('FIM!')
    print('=' * 40)
    print("Contagem de 10 até 0 de 2 em 2")
    for c in range(10, -1, -2):
        print(c, end=' ')
        sleep(0.1)
    print('FIM!')
    print('=' * 40)
    print('Agora é sua vez de personalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim:  '))
    p = int(input('Passo:  '))
    if p == 0:
        p = 1
    if i > f:
        f = f - 1
        if p > 0:
            p = -p
    else:
        f = f + 1
        if p < 0:
            i = f
            f = i + 1
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.1)
    print('FIM!')


# Programa Principal
contador(i,f,p)