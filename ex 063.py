print('='*10, 'SEQUÊNCIA DE FIBONACCI', '='*10)
termos = int(input('Quantos termos você quer mostrar? '))
contador = 3
primeiro = 0
segundo = 1
print('='*44)
print('{} -> {} ->'.format(primeiro, segundo), end=' ')
while contador <= termos:
    terceiro = primeiro + segundo
    print('{} ->'.format(terceiro), end=' ')
    primeiro = segundo
    segundo = terceiro
    contador += 1
print('FIM')