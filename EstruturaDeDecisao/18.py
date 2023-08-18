# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])
valida = True

if mes < 1 or mes > 12:
    valida = False
elif mes == 2:
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                bissexto = True
            else:
                bissexto = False
        else:
            bissexto = True
    else:
        bissexto = False
    if bissexto:
        if dia < 1 or dia > 29:
            valida = False
    else:
        if dia < 1 or dia > 28:
            valida = False
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    if dia < 1 or dia > 31:
        valida = False
else:
    if dia < 1 or dia > 30:
        valida = False
        