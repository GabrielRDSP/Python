nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f"Media: {media}")
    print("Você foi reprovado!")
elif media == 5.0 and 6.9:
    print(f"Media: {media}")
    print("Recuperação...")
else:
    print(f"Media: {media}")
    print("Você foi aprovado!")