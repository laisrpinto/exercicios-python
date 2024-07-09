from math import hypot
co = float(input("Qual o comprimento do cateto oposto? "))
ca = float(input("Qual o comprimento do cateto adjacente? "))
hipotenusa = hypot(co, ca)
print("A hipotenusa é {:.2f}".format(hipotenusa))
