salario = int(input("Digite seu salario: R$"))
if salario >= 1250:
    aumento = salario * 10 / 100
    print(f"Seu salario de R${salario} com um aumento de 10% fica: R${salario + aumento:.0f}")
if salario < 1250:
    aumento = salario * 15 / 100
    print(f"Seu salario de R${salario} com um aumento de 15% fica: R${salario + aumento:.0f}")


