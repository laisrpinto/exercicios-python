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

