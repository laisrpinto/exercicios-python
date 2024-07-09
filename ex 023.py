#num = str(input('Digite um número de 0 a 9999 '))
#unidade = num[3]
#dezena = num[2]
#centena = num[1]
#milhar = num[0]
#print(unidade,dezena, centena, milhar)
num = int(input("Digite um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("A unidade é {}".format(u))
print("A dezena é {}".format(d))
print("A centena é {}".format(c))
print("O milhar é {}".format(m))