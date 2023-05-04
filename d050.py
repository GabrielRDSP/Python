cont = 0
soma = 0
for c in range(0,6):
    numero = int(input("Digite um valor: "))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print(f"Você informou {cont} numeros PARES, a soma de todos eles é: {soma}")

