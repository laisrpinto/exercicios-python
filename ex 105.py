def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: um ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não mostrar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


# Programa Principal
print(notas(8, 9, 9, 9.5, 9.9, sit=True))
help(notas)