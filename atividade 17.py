###
# atividade 16
# aluno: Apollo
# Data: 08/04/2024
## Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo.

print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

numero_op = int(input("Digite o número da operação desejada (1 a 4): "))
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if numero_op == 1:
    resultado = valor1 + valor2
elif numero_op == 2:
    resultado = valor1 - valor2
elif numero_op == 3:
    resultado = valor1 * valor2
elif numero_op == 4:
    if valor2 != 0:
        resultado = valor1 / valor2

print(f"Resultado da operação: {resultado:.2f}")