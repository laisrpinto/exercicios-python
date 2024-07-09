'''n = soma = contador = 0
while n != 999:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'Voce digitou {contador} números e a soma é {soma}.')'''

#SOLUÇÃO GUANABARA:
soma = cont = 0
while True: #NESSE CASO, EU NÃO PRECISO INICIAR A VARIÁVEL, COMO NOS EXERCICIOS ANTERIORES
    n = int( input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} valores é {soma}')
