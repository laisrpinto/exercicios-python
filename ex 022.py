#nome = str(input('Digite seu nome completo '))
#print('Maiscula',nome.upper())
#print(nome.lower())
#print(len(nome.replace(" ", "")))
#print(len(nome.split()[0]))

nome = str(input("Digite o nome da pessoa: ")).strip()
print("Seu nome em maiusculo é {}".format(nome.upper()))
print("Seu nome em minúsculo é {}".format(nome.lower()))
print("Seu nome tem {} letras".format(len(nome) - nome.count(" ")))
#print("Seu primeiro nome tem {} letras".format(nome.find(" ")))    OU:
lista = nome.split()
print(lista)
print("Seu primeiro nome é {} e tem {} letras".format(lista[0],len(nome.split()[0])))
