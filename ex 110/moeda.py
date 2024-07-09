def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else cifrao(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if not formato else cifrao(res) #Opção alternativa


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else cifrao(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else cifrao(res)


def cifrao(preco=0, cifrao='R$'):
    res = f'{cifrao}{preco:>.2f}'.replace('.', ',')
    return res


def resumo(valor=0, aumento=10, reducao=5):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado":<}: \t{cifrao(valor):>10}')
    print(f'{"Dobro do preço":<}: \t{dobro(valor, True):>10}')
    print(f'Metade do preço: \t{metade(valor, True):>10}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(valor, reducao, True)}')
    print('-' * 30)

