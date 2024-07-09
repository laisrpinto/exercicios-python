print('{:=^100}'.format(' VAMOS FALAR SOBRE PROGESSÃO ARITMÉTICA?! '))
primeiro = int(input("Qual o primeiro termo da PA? "))
razão = int(input('Qual a razão dessa PA? '))
for termo in range(1, 11):
    termo = primeiro +(termo - 1)*razão
    print(termo, end=' ')
