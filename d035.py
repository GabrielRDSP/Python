r1 = int(input("Digite o valor da reta 1: "))
r2 = int(input("Digite o valor da reta 2: "))
r3 = int(input("Digite o valor da reta 3: "))
if r3 + r2 > r1 and r2 + r1 > r3 and r1 + r3 > r2:
    print("É possivel fazer um triangulo com essas medidas!!!")
else:
    print("Não é possivel fazer um triangulo com essas medidas!!!")