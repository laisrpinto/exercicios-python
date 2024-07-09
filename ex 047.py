'''for c in range (1, 51):
    if c % 2 == 0:
        print(c, end=' ')'''

#ALTERNATIVA (NESSA SOLUÇÃO O PROCESSADOR OCUPA METADE DO TEMPO PQ NÃO PRECISA VERIFICAR DE UM EM UM:
#É POSSÍVEL VERIFICAR ISSO PRINTANDO UM PONTO SE EU QUISER, AQUI NÃO FIZ
print('='*25, end=' ')
for c in range (2, 51, 2):
    print(c, end=' ')
print('='*25)