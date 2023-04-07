produto = float(input("Coloque o preço do produto R$"))
desconto = 5
porcentagem = 100
novo = produto - (produto * desconto / porcentagem)
print(f"O seu produto com R${desconto} de desconto custa:R${novo}")