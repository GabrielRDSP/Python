frase = str(input("Digite uma frase: "))
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Essa frase é um Palíndromo!")
else:
    print("Essa frase não é um Palindromo!")

