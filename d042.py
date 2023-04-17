r1 = int(input("Valor da reta 1: "))
r2 = int(input("Valor da reta 2: "))
r3 = int(input("Valor da reta 3: "))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print("É possivel formar um triangulo ", end="")
    if r1 == r2 == r3:
        print("EQUILATERO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
    print("Não é possivel formar um triangulo!!")