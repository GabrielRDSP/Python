from datetime import date
data = int(input("Informe sua data de nascimento: "))
ano = date.today().year
idade = ano - data
if idade <= 9:
    print(f"Sua idade é {idade}!")
    print("Categoria: MIRIM")
elif idade <= 14:
    print(f"Sua idade é {idade}!")
    print("Categoria: INFANTIL")
elif idade <= 19:
    print(f"Sua idade é {idade}!")
    print("Categoria: JUNIOR")
elif idade <= 20:
    print(f"Sua idade é {idade}!")
    print("Categoria: SÊNIOR")
else:
    print(f"Sua idade é {idade}!")
    print("Categoria: MASTER")
