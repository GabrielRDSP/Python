nome = str(input("Digite seu nome completo: ")).strip()
print(f"Seu nome em maiúsculas é: {nome.upper()}")
print(f"Seu nome em minúsculas é: {nome.lower()}")
print(f"Seu nome possui {len(nome) - nome.count(' ')} letras")
frase = nome.split()
print(f"O seu primeiro nome é {frase[0]} e ele possui {len(frase[0])} letras")

