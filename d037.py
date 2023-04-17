num = int(input("Digite um numero inteiro: "))
print("""Escolhe uma das bases para conversão: 
[ 1 ] Binário 
[ 2 ] Octal
[ 3 ] Hexadecimal""")
opção = int(input("Sua opção: "))
if opção == 1:
    binario = bin(num)
    print(f"A conversão do numero {num} para Binario é: {binario[2:]}")
elif opção == 2:
    octal = oct(num)
    print(f"A conversão do numero {num} para Octal é: {octal[2:]}")
elif opção == 3:
    hexadecimal = hex(num)
    print(f"A conversão do numero {num} para Hexadecimal é: {hexadecimal[2:]}")
else:
    print("Opção invalida!!!")
