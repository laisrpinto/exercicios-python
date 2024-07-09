from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.cifrao(p, "€")} é {moeda.cifrao(moeda.metade(p), "U$")}')
print(f'O dobro de {moeda.cifrao(p)} é {moeda.cifrao(moeda.dobro(p))}')
print(f'Aumentando {moeda.cifrao(p)} em 10%, temos {moeda.cifrao(moeda.aumentar(p, 10))}')