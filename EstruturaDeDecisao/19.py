"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

numero = int(input("Digite um número inteiro menor que 1000: "))
if numero < 1000:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10
    if centenas == 1:
        centenas = str(centenas) + " centena"
    else:
        centenas = str(centenas) + " centenas"
    if dezenas == 1:
        dezenas = str(dezenas) + " dezena"
    else:
        dezenas = str(dezenas) + " dezenas"
    if unidades == 1:
        unidades = str(unidades) + " unidade"
    else:
        unidades = str(unidades) + " unidades"
    print(f"{centenas}, {dezenas} e {unidades}")