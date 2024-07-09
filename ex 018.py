import math
valor = float(input("Digite o valor do angulo: "))
angulo = math.radians(valor)
print("O angulo que você digitou foi {:.2f}. \n"
      " o seno é {:.2f} \n "
      "o coseno é {:.2f} \n"
      "e a tangente é {:.2f}".format(valor, math.sin(angulo), math.cos(angulo), math.tan(angulo)))