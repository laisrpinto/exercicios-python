def leiaInt(inte):
    ok = False
    while True:
        try:
            inteiro = int(input(inte))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\33[m')
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return inteiro


def leiaReal(real1):
    while True:
        try:
            real = float(input(real1).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.\33[m')
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return real


#Programa Principal
n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaReal('Digite um número Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')