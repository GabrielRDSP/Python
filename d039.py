from datetime import date
data = int(input(f"Informe sua data de nascimento: "))
ano = date.today().year
idade = ano - data
alistar = 18 - idade
if idade < 18:
    print("Você Ainda precisa se alistar!!")
    print(f"Você ainda tem {alistar} ano/anos pra se alistar.")
elif idade == 18:
    print("Você devera se alistar!!")
elif idade > 18:
    alistar = idade - 18
    print(f"Você passou {alistar} ano/anos do prazo de alistamento...")
