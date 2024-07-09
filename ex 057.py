sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
