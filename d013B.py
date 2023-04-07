produto = int(input("Digite o preço do seu produto R$:"))
desconto = 10
aumento = 10
porcentagem = 100
final_desconto = produto - (produto * desconto / porcentagem)
final_aumento = produto + (produto * desconto / porcentagem)
print(f"Seu produto que custa: R${produto} comprado a vista, com desconto adicional, agora custa: {final_desconto}")
print(f"Seu produto que custa: R${produto} comprado parcelado, com aumento adicional, agora custa: {final_aumento}")