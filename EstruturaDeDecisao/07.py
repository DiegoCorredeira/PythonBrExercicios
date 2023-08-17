# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))
num3 = int(input("Informe outro número: "))

maior = 0 

if num1 < num2 and num1 < num3:
    maior = num1
elif num2< num1 and num2< num3:
    maior = num2
elif num3< num1 and num3< num2:
    maior = num2

print(f'O menor número entre {num1}, {num2} e {num3} é {maior}')