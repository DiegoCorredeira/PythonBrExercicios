"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

"""
combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ")
litros = float(input("Digite a quantidade de litros: "))
if combustivel == "A":
    if litros <= 20:
        preco = litros * 1.90
        desconto = litros * 0.03
    else:
        preco = litros * 1.90
        desconto = litros * 0.05
elif combustivel == "G":
    if litros <= 20:
        preco = litros * 2.50
        desconto = litros * 0.04
    else:
        preco = litros * 2.50
        desconto = litros * 0.06
else:
    print("Tipo de combustível inválido.")
    preco = 0
    desconto = 0
print(f"Preço: {preco}")
print(f"Desconto: {desconto}")
print(f"Valor a pagar: {preco - desconto}")
