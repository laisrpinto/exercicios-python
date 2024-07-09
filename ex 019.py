import random
n1 = input("Digite o nome do primeiro aluno: ")
n2 = input("Digite o nome do segundo aluno: ")
n3 = input("Digite o nome do terceiro aluno: ")
n4 = input("Digite o nome do quarto alune: ")
list = [n1, n2, n3, n4]
escolhido = random.choice(list)
print("O alune escolhido foi {}".format(escolhido))