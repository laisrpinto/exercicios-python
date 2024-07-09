palavras = ('aprender', 'programar', 'linguagem', 'python','curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
'''a = e = i = o = u = 0
for c in range(0, len(palavras)):
    print(f'Na palavra {palavras[c].upper()}', end=' ')
    a = palavras[c].count('a')
    e = palavras[c].count('e')
    i = palavras[c].count('i')
    o = palavras[c].count('o')
    u = palavras[c].count('u')
    if a > 0 or e > 0 or e > 0 or i > 0 or u > 0:
        print('a ' * a,'e ' * e, 'i ' * i, 'o ' * o, 'u ' * u,)
    else:
        print('')'''

#SOLUÇÃO GUANABARA:

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')



