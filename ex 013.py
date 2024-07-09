salario = float(input("Qual o salário do funcionário? €"))
aumento = salario + (salario * 15/100)
print("O funcionário que ganhava {:.2f}, com 15% de aumento vai passar a ganhar {:.2f}".format(salario, aumento))