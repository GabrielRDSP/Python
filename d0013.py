al = int(input("Qual a altura da sua parede?: "))
lar = int(input("Qual a largura da sua parede? "))
tinta = 2
area = al * lar
print(f"A quantidade necessaria de tinta para preencher a area de {area}m² é {area / tinta:.0f}l")