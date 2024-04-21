###
# atividade 05
# aluno: Apollo
# Data: 08/04/2024
##Faça um programa que receba um número inteiro e verificado se este número é par ou ímpar.add()

numero = int(input("digite um numero:"))

resultado = numero % 2

if resultado == 0:
    print("É par")
else:
    print("É impar")