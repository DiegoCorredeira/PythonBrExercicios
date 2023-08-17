# Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Digite o primeiro número: "))

num2 = int(input("Digite o segundo número: "))

# Verifica qual é o maior número
if num1 > num2:
    print("O primeiro número é o maior: ", num1)
elif num2 > num1:
    print("O segundo número é o maior: ", num2)
else:
    print("Os números são iguais: ", num1, " = ", num2)

# Pode-se também utilizar a função max() para encontrar o maior número
# print("O maior número é: ", max(num1, num2))

