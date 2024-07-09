def linha(tam=42):
    return '-'* tam


def cabecalho(msg=''):
    print(linha())
    print(msg.center(42))
    print(linha())
    print(f'\033[33m1\33[m - \033[34mVer pessoas cadastradas\33[m')
    print(f'\033[33m2\33[m - \033[34mCadastrar nova Pessoa\33[m')
    print(f'\033[33m3\33[m - \033[34mSair do Sistema\33[m')
    print(linha())


def menu(msg=''):
    cabecalho('MENU PRINCIPAL')
    res =''
    while True:
        try:
            res = int(input(f'\033[33m{msg}\33[m'))
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar uma opção')
            break
        except:
            print('\033[31mERRO!Opção inválida. Tente novamente.')
        else:
            if 1 <= res <= 3:
                return res
            else:
                print('\033[31mERRO!Opção inválida. Tente novamente.')
                continue
    return res
    print(linha())


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
