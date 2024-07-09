from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual. '))
#Condição para 0 ser o ano atual:
if ano == 0:
    ano = date.today().year
#Cálculos para saber se o ano é bissexto:
four = ano % 4
cem = ano % 100
qua = ano % 400
if four==0 and cem!=0 or four==0 and cem==0 and qua==0:
    print('O ano {} é bissexto.'.format(ano))

else:
    print('O ano {} não é bissexto.'.format(ano))