###
# atividade 15
# aluno: Apollo
# Data: 08/04/2024
##Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou por 5, mas não simultaneamente pelos dois.

numero = int(input("Digite um número inteiro: "))

if numero % 3 == 0 and numero % 5 != 0:
    print(f"{numero} é divisível por 3, mas não por 5.")
elif numero % 5 == 0 and numero % 3 != 0:
    print(f"{numero} é divisível por 5, mas não por 3.")
else:
    print(f"{numero} não é divisível por nenhum. ")