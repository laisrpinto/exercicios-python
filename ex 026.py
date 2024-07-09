#frase = str (input('Digite uma frase ')).strip().lower()
#print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
#print('A primeira letra A apareceu na {} posição.'.format(frase.find('a')+1))
#print('A ultima letra A apareceu na {} posição.'.format(frase.rfind('a')+1))

nome = str(input("Digite um nome qualquer: ")).strip().lower()
letraA= nome.count("a")
primeira = nome.find("a")
ultima = nome.rfind("a")
print("A letra A aparece {} vezes \n" 
      "A primeira vez que ela apereceu foi na posição {}\n"
      "A ultima vez que ela apareceu foi na posição {}".format(letraA, primeira, ultima))
