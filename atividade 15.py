###
# atividade 15
# aluno: Apollo
# Data: 08/04/2024
##Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este número. Isto é, janeiro se 1, fevereiro se 2, e assim por diante

numero_mes = int(input("Digite um número inteiro entre 1 e 12: "))

if numero_mes == 1:
    print("Janeiro")
elif numero_mes == 2:
    print("Fevereiro")
elif numero_mes == 3:
    print("Março")
elif numero_mes == 4:
    print("Abril")
elif numero_mes == 5:
    print("Maio")
elif numero_mes == 6:
    print("Junho")
elif numero_mes == 7:
    print("Julho")
elif numero_mes == 8:
    print("Agosto")
elif numero_mes == 9:
    print("Setembro")
elif numero_mes == 10:
    print("Outubro")
elif numero_mes == 11:
    print("Novembro")
elif numero_mes == 12:
    print("Dezembro")
else:
    print("Não existe mês com este número.")