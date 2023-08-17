# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))
num3 = int(input("Informe outro número: "))

maior = 0
menor = 0
meio = 0

if num1 > num2 and num1 > num3:
    maior = num1
    if num2 > num3:
        meio = num2
        menor = num3
    else:
        meio = num3
        menor = num2
elif num2 > num1 and num2 > num3:
    maior = num2
    if num1 > num3:
        meio = num1
        menor = num3
    else:
        meio = num3
        menor = num1
elif num3 > num1 and num3 > num2:
    maior = num3
    if num1 > num2:
        meio = num1
        menor = num2
    else:
        meio = num2
        menor = num1

print(f'Os números em ordem decrescente são: {maior}, {meio} e {menor}')