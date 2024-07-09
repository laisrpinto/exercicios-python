largura = float(input("Qual a largura da sua parede? "))
altura = float(input("Qual a altura da sua parede? "))
area = largura * altura
tinta = area / 2
print("Sua parede tem {} metros quadrados. Para pinta-la irá precisar de {} litros de tinta".format(area, tinta))
