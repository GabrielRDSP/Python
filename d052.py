from colorama import Fore,Style
num = int(input("Digite um numero: "))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(Fore.BLUE, end = " ")
        total += 1
    else:
        print(Fore.RED, end = " ")
    print(f"{c}", end=" ")
print(Style.RESET_ALL,f"\nO numero {num} foi divisivel {total} vezes")
if total == 2:
    print(f"E por isso o numero {num} É PRIMO")
else:
    print(f"E por isso o numero {num} NÃO É PRIMO")