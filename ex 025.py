#nome = str (input('Digite seu nome completo ')).upper()
#print('Seu nome tem Silva?','SILVA' in nome)


nome = str(input("Digite um nome completo: ")).strip()
minu = nome.lower()
verif = "silva" in minu
print("Seu nome teu ´Silva´? {}".format(verif))
