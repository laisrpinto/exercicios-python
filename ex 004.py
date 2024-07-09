a = input("Digite algo aí minha parceira: ")
print(f'''
      Qual o tipo primitivo? {type(a)}
      É numérico? {a.isnumeric()}
      É alfabético? {a.isalpha()}
      Está em maiúscula? {a.isupper()}
      Está em minúscula? {a.islower()}
      Está capitalizada? {a.istitle()}
      É um espaço? {a.isspace()}''')
