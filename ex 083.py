expressao = str(input('Digite a expressão: '))
abertos = []
fechados = []
for c, i in enumerate(expressao):
    if i == '(':
        abertos.append(i)
    elif i == ')':
        fechados.append(i)
if len(abertos) == len(fechados):
    print('Sua expressão é válida.')
else:
    print('Sua expressão é inválida.')
