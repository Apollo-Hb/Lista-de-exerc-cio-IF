###
# atividade 09
# aluno: Apollo
# Data: 08/04/2024
##Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima: “Empréstimo não concedido”, caso contrário imprima: “Empréstimo concedido”.

trabalhador = input("Digite o nome do funcionario:")
salario = float(input("Digite o salario do funcionario:"))
prestação = float(input("Digite o valor da prestação:"))

if prestação > ( salario * 0.20):
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")