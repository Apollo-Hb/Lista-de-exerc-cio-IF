###
# atividade 02
# aluno: Apollo
# Data: 08/04/2024
##Leia um número fornecido pelo usuário. Se esse numero for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

import math

numero = float(input("digite um  numero: "))

if numero > 0:
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero:.2f} eh: {raiz}")
elif numero < 0:
    print(f"esse {numero} é negativo")