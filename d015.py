dias = int(input("Quantos dias seu carro foi alugado? "))
km = float(input("Quantos quilometros foram percorridos? "))
carro = 60
preço_dias = carro * dias
km_p = 0.15
preço_km = km_p * km
preço_final = preço_dias + preço_km
print(f"O preço do carro alugado em dias é: R${preço_dias}")
print(f"O preço dos quilometros percorridos em dias é: R${preço_km}")
print(f"E o total fica: R${preço_final}")