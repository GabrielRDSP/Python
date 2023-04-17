salario = float(input("O valor do salario: R$"))
casa = float(input("O valor da casa: R$"))
anos = int(input("Em quantos anos você quer financiar: "))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print(f"Para pagar uma casa de {casa:.2f} em {anos} anos a prestação sera de R${prestação:.2f}")
if prestação <= minimo:
    print("Emprestimo Concedido!!!")
else:
    print("Emprestimo Negado!!!")
