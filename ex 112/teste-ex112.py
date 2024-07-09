from ex112.utilidadescemv import dados
from ex112.utilidadescemv import moeda
p = dados.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 90, 5)