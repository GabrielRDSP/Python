import math
angulo = float(input("Digite o numero de um angulo qualquer: "))
coss = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print(f"O ângulo de {angulo} possui o SENO de: {seno:.2f}")
print(f"O ângulo de {angulo} possui o COSSENO de: {coss:.2f}")
print(f"O ângulo de {angulo} possui a TANGENTE de: {tang:.2f}")
