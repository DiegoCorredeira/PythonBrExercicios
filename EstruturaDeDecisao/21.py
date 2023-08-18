"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

valor = int(input("Digite o valor do saque: "))
if valor < 10 or valor > 600:
    print("Valor inválido.")
else:
    notas100 = valor // 100
    valor = valor % 100
    notas50 = valor // 50
    valor = valor % 50
    notas10 = valor // 10
    valor = valor % 10
    notas5 = valor // 5
    valor = valor % 5
    notas1 = valor
    print(f"Notas de 100: {notas100}")
    print(f"Notas de 50: {notas50}")
    print(f"Notas de 10: {notas10}")
    print(f"Notas de 5: {notas5}")
    print(f"Notas de 1: {notas1}")