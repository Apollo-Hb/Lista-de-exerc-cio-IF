###
# atividade 06
# aluno: Apollo
# Data: 08/04/2024
##Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,assim como a diferença existente entre ambos.

num1 = float(input("digite um  numero: "))
num2 = float(input("digite um  numero: "))
diferença = num1 - num2
print(f"a diferença entre os numeros será: {diferença:.2f}")
if num1 > num2:
    print(f"O {num1 or num2:.2f} sera o maior.")
elif num1 < num2:
    print(f"O {num1 or num2:.2f} sera o maior. ")