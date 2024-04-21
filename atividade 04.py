###
# atividade 04
# aluno: Apollo
# Data: 08/04/2024
##Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre a. O número digitado ao quadradob. A raiz quadrada do número digitado.

import math

numero = float(input("digite um  numero: "))

if numero > 0:
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero:.2f} eh: {raiz}")
    quadrado = numero ** 2
    print(f"o quadrado do {numero:.2f} eh: {quadrado:.2f}")
elif numero < 0:
    print(f" o {numero} digitado eh negativo.")