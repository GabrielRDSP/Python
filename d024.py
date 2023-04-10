cd = str(input("Digite o nome da sua cidade: ")).strip()
print("Iremos verificar se sua cidade começa com Santo no nome...")
cdl = cd.lower()
print(cdl[:5] == 'santo')