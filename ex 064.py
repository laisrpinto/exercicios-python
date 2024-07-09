num = soma = contador = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(contador, soma))

#O programa vai contar só o que tá dentro, e como coloquei o num por ultimo, se eu digitar 999 ele não vai pra soma