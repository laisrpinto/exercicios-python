from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.cifrao(p, "€")} é {moeda.metade(p, formato=True)}')
print(f'O dobro de {moeda.cifrao(p)} é {moeda.dobro(p, formato=False)}')
print(f'Aumentando {moeda.cifrao(p)} em 10%, temos {moeda.aumentar(p, 10, formato=True)}')