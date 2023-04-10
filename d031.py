km = float(input("Digite a distancia da sua viagem em km: "))
if km <= 200:
    preço = km * 0.50
    print(f"O valor de sua viagem curta fica: R${preço:.2f}")
else:
    preço = km * 0.45
    print(f"O valor de sua viagem longa fica: R${preço:.2f}")

