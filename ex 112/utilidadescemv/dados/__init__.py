'''def leiaDinheiro(texto):
    res = str(input(texto).replace(',', '.'))
    while True:
        if res.isalpha():
            print(f'\033[31mERRO: {res} é um preço inválido!\033[m')
            res = input(texto).replace(',', '.')
        elif float(res):
            break
    return float(res)'''

# SOLUÇÃO GUANABARA:


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\33[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)




    