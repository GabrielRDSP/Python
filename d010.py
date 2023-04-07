num = int(input("Digite o valor que você possui na sua carteira? R$"))
dolar = 5.05
euro = 5.52
iene = 0.038
re = num / euro
rd = num / dolar
ri = num / iene
print(f"R${num} Equivale a ${rd:.2f}")
print(f"R${num} Equivale a €{re:.2f}")
print(f"R${num} Equivale a ¥{ri:.2f}")