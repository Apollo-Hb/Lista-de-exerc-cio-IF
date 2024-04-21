###
# atividade 19
# aluno: Apollo
# Data: 08/04/2024
##Dados três valores A, B, C, verificar se eles podem ser valores dos lados de um triangulo e se forem, se é um triangulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos: O comprimento de cada lado de um triangulo é menor que a soma dos outros dois lados. Chama-se equilátero o triangulo que tem três lado iguais. Denominam-se isósceles o triangulo que tem o comprimento de dois lados iguais Recebe o nome de escaleno o triangulo que tem os três lados diferentes.

A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))

if A + B > C and A + C > B and B + C > A:
    if A == B == C:
        print("É um triângulo equilátero.")
    elif A == B or A == C or B == C:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")