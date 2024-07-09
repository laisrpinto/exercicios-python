#cidade = str(input('Em qual cidade você nasceu? ')).strip()
#print(cidade[:5].upper() == 'SANTO')

cidade = str(input("Digite o nome da cidade que tu nasceu: ")).strip()
minuscula = cidade.lower()
separa = minuscula.split()
verificacao = separa[0] == "santo"
if verificacao == True:
    print("A cidade que tu nasceu é verdadeira")
else:
    print("A cidade que tu nasceu é falsa")

