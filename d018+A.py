import math
angulo = float(input("Digite o numero de um angulo qualquer: "))
coss = math.cos(math.radians(angulo)) #math.cos = Cosseno
seno = math.sin(math.radians(angulo)) #math.sin = Seno
tang = math.tan(math.radians(angulo)) #math.tan = Tangente
print(f"O ângulo de {angulo} possui o SENO de: {seno:.2f}")
print(f"O ângulo de {angulo} possui o COSSENO de: {coss:.2f}")
print(f"O ângulo de {angulo} possui a TANGENTE de: {tang:.2f}")
