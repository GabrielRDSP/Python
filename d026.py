frase = str(input("Digite uma frase: ")).strip().upper()
print(f"Na sua frase, aparece {frase.count('A')} a letra A")
print(f"A primeira posição da letra A foi: {frase.find('A') + 1}")
print(f"A ultima posição da letra A foi: {frase.rfind('A') + 1}")