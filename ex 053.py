frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('é palindromo')
else:
    print('não é palindromo')






'''frase = str(input('Digite uma frase: ')).strip().upper()
invertida = frase[::-1]
print(invertida)'''

