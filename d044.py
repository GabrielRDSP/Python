valor_produto = int(input("Digite o valor do seu produto: R$"))
print(f"O preço do seu produto é: R${valor_produto}")
print("""Escolha o metodo de pagamento:
[ 1 ] Á Vista Dinheiro/Cheque: 10% de desconto
[ 2 ] Á Vista Cartão: 5% de desconto
[ 3 ] Em ate 2x no Cartão: Preço normal
[ 4 ] 3x ou mais no Cartão: 20% de Juros""")
escolha = int(input("Escolha: "))
if escolha == 1:
    print(f"O seu produto com 10% de desconto fica: R${valor_produto - (valor_produto * 10 / 100):.2f}")
elif escolha == 2:
    print(f"O seu produto com 5% de desconto fica: R${valor_produto - (valor_produto * 5 / 100):.2f}")
elif escolha == 3:
    print(f"Você pagou o preço normal do produto.")
elif escolha == 4:
    print(f"O seu produto com 20% de aumento fica: R${valor_produto + (valor_produto * 20 / 100)}")