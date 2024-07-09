real = float(input("Quantos reais tu tem na carteira? R$"))
euro = real / 5.34
dolar = real / 4.92
print("Com R${:.2f} reais, tu consegue comprar €{:.2f} euros ou U${:.2f} dolares".format(real, euro, dolar))