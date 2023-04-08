import math
co = float(input("Comprimento do Cateto oposto: "))
ca = float(input("Comprimento do Cateto adjacente: "))
ch = math.hypot(co,ca)
#ch = (co ** 2 + ca ** 2) ** (1/2)
#print(f"A hipotenusa do triangulo vai medir: {ch:.2f}")
print(f"A hipotenusa do triangula vai medir: {ch:.2f}")