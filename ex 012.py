preco = float(input("Qual o preço do produto? €"))
novo = preco - (preco * 0.05)
print("O produto que custava {}, com a promoção de 5% de desconto vai custar {:.2f}".format(preco, novo))