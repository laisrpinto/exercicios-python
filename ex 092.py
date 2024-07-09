import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
trabalhador['idade'] = datetime.date.today().year - ano
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = (trabalhador['contratação'] - ano) + 35
print('-='*30)
for k, v in trabalhador.items():
    print(f' - {k} tem o valor {v}')