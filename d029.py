from colorama import Fore
n = int(input(Fore.BLUE + "Digite a velocidade que seu carro esta percorrendo: "))
if n <=80:
    print(Fore.GREEN + "Tenha um bom dia! Dirija com segurança!!")
else:
    print(Fore.RED + "Você foi multado!!!")
    print(Fore.YELLOW + f"Você tera que pagar: R${(n - 80) * 7}")