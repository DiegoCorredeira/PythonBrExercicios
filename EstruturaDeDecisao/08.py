# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco_um = input("Informe o preço do primeiro produto: ")
preco_dois = input("Informe o preço do segundo produto: ")
preco_tres = input("Informe o preço do terceiro produto: ")

if preco_um < preco_dois and preco_um < preco_tres:
    print("O primeiro produto é o mais barato")
elif preco_dois < preco_um and preco_dois < preco_tres:
    print("O segundo produto é o mais barato")
elif preco_tres < preco_um and preco_tres < preco_dois:
    print("O terceiro produto é o mais barato")