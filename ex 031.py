distancia = float(input('Qual a distancia da sua viagem em km? '))

if distancia <= 200:
    curta = distancia * 0.5
    print('Sua viagem é curta. Você pagará R$0,5 por KM. No total será R${}.'.format(curta))
else:
    longa = distancia * 0.45
    print('Sua viagem é longa. Você vai pagar R$0,45 por KM. No total será R${}.'.format(longa))