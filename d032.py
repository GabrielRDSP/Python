from datetime import date
ano = int(input("Digite o ano que você quer analisar, ou digite 0 para analisar o seu ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"Esse ano de {ano} é Bissexto")
else:
    print(f"Esse ano de {ano} não é Bissexto")