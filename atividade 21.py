###
# atividade 21
# aluno: Apollo
# Data: 08/04/2024
##Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996.

ano = int(input("Informe o ano:"))

if ano % 4==0 or ano % 400==0:
    print("esse ano é bissexto")
else:
    print("esse ano não é bissexto")
