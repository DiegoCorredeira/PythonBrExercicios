# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

valor_um = int(input("Digite o primeiro valor inteiro: "))
valor_dois = int(input("Digite o segundo valor inteiro: "))
valor_tres = float(input("Digite o terceiro valor real: "))
produto = (valor_um * 2) * (valor_dois / 2)
soma = (valor_um * 3) + valor_tres
cubo = valor_tres ** 3

print(f"O produto do dobro do primeiro com metade do segundo é {produto}")
print(f"A soma do triplo do primeiro com o terceiro é {soma}")