# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
nota_tres = float(input("Digite a terceira nota: "))
nota_quatro = float(input("Digite a quarta nota: "))

media = (nota_um + nota_dois + nota_tres + nota_quatro) / 4

print(f"A média das notas é {media}")