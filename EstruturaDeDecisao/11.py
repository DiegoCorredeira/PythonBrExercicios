"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

salario = float(input("Informe o salário do colaborador: "))
percentual = 0
aumento = 0

if salario <= 280:
    percentual = 20
    aumento = salario * 0.2
elif salario > 280 and salario <= 700:
    percentual = 15
    aumento = salario * 0.15
elif salario > 700 and salario <= 1500:
    percentual = 10
    aumento = salario * 0.1
elif salario > 1500:
    percentual = 5
    aumento = salario * 0.05

print(f"Salário antes do reajuste: R$ {salario}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento}")
print(f"Novo salário: R$ {salario + aumento}")
