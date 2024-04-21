###
# atividade 03
# aluno: Apollo
# Data: 08/04/2024
##Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o número ao quadrado
import math

numero = float(input("digite um  numero real: "))

if numero > 0:
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} eh: {raiz}")
elif numero < 0:
    quadrado = numero ** 2
    print(f"o quadrado do {numero} negativo eh: {quadrado}")