termo = int(input("Digite o primeiro termo: "))
razão = int(input("Digite a razão: "))
décimo = termo + (11 - 1) * razão
for c in range(termo,décimo,razão):
    print(f"{c}", end = " → ")
print("Acabou")