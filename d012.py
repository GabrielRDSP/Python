num = int(input("Digite o preço do seu produto: "))
desconto = 5
porcentagem = 100
final = num - (num * desconto / 100)
print(f"Seu produto que custa R${num} com 5% de desconto agora custa: R${final}")