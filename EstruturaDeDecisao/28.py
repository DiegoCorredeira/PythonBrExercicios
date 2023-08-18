"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

tipoCarne = input("Digite o tipo de carne (F-file duplo, A-alcatra, P-picanha): ")
quantidade = float(input("Digite a quantidade (em Kg): "))
cartaoTabajara = input("Cartão Tabajara? (S-sim, N-não): ")
if tipoCarne == "F":
    if quantidade <= 5:
        preco = quantidade * 4.90
    else:
        preco = quantidade * 5.80
elif tipoCarne == "A":
    if quantidade <= 5:
        preco = quantidade * 5.90
    else:
        preco = quantidade * 6.80
elif tipoCarne == "P":
    if quantidade <= 5:
        preco = quantidade * 6.90
    else:
        preco = quantidade * 7.80
else:
    print("Tipo de carne inválido.")
    preco = 0
if cartaoTabajara == "S":
    desconto = preco * 0.05
else:
    desconto = 0
print(f"Tipo de carne: {tipoCarne}")
print(f"Quantidade: {quantidade}")
print(f"Preço: {preco}")
print(f"Cartão Tabajara: {cartaoTabajara}")
print(f"Desconto: {desconto}")
print(f"Valor a pagar: {preco - desconto}")
