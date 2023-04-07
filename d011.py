al = float(input("Qual a altura da sua parede?: "))
lar = float(input("Qual a largura da sua parede? "))
area = al * lar
print(f"Sua parede possui uma dimensão de {al}x{lar} e sua area é de {area}m²")
tinta = 3
print(f"Sera necessario {area / tinta}m² de tinta para pintar essa parede")

