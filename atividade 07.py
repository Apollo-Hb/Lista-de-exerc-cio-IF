###
# atividade 07
# aluno: Apollo
# Data: 08/04/2024
##Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem “Números iguais"

num1 = float(input("digite um  numero: "))
num2 = float(input("digite um  numero: "))

if num1 > num2:
    print(f"O {num1 or num2:.2f} sera o maior.")
elif num1 < num2:
    print(f"O {num1 or num2:.2f} sera o maior. ")
else:
    print(" são numeros iguais")
