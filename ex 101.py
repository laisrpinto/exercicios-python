'''def voto(ano):
    voto = ''
    if idade < 16:
        voto = 'NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 70:
        voto = 'VOTO OPCIONAL.'
    else:
        voto = 'VOTO OBRIGATÓRIO.'
    return voto

nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - nasc
print(f'Com {idade} anos: {voto(nasc)}')'''

# SOLUÇÃO GUANABARA:


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))



