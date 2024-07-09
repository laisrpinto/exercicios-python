pessoas = list()
pessoa = dict()
sum = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        print('ERRO! Por favor, digite apenas F OU M.')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    sum += pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    resp = str(input('Quer contianuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer contianuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'B) A média de idade é {sum/len(pessoas)}')
print(f'C) As mulheres cadastradas foram ', end=' ')
for p in pessoas:
    if p['sexo'] in 'F':
        print(p["nome"], end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] > (sum/len(pessoas)):
        for k, v in p.items():
            print(f'  {k} = {v}; ', end=' ')
        print()







