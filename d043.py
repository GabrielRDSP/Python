altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
IMC = peso / (altura**2)
print(f"Seu IMC é: {IMC:.1f}")
if IMC < 18.5:
    print("Você esta abaixo do peso normal.")
elif IMC >= 18.5 and IMC < 25:
    print("Você esta no peso ideal!")
elif IMC >= 25 and IMC < 30:
    print("Você esta acima do peso ideal.")
elif IMC >= 30 and IMC < 40:
    print("Você esta acima obeso.")
elif IMC >=40:
    print("Você esta em um estado critico de obesidade!")