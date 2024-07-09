#nome = str(input('Digite seu nome completo ')).strip().split()
#print('Muito prazer em te conhecer!')
#print('Seu primeiro nome é {}'.format(nome[0]))
#print('Seu último nome é {}'.format(nome[-1]))

nome= str(input("Escreve seu nome completo, por favor: "))
nomecorreto = nome.strip().upper()
separa = nome.split()
primeiro = separa[0].capitalize()
ultimo = separa[-1].capitalize()
meio = nomecorreto.count(" ")
print(meio)



