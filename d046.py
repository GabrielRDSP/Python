from time import sleep
import emoji
print("Contagem Regresiva para o lançamento dos fogos de artificio:")
print("-"*12)
for c in range(10, 0, -1):
    sleep(1)
    print(f"{c:>6}")
sleep(1)
print("-"*12)
print(emoji.emojize(":party_popper::party_popper:Fogos de artificio lançados!!!:party_popper::party_popper:"))