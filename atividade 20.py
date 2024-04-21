###
# atividade 20
# aluno: Apollo
# Data: 08/04/2024
##Leia a idade e o tempo de serviço de um trabalhador e escreve se ele pode ou não se aposentar. As condições para aposentadoria são: a. Ter pelo menos 65 anos b. Ou ter trabalhado pelo menos 30 anos c. Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

nome = int(input("Digite o nome do trabalhador: "))
idade = int(input("Digite a idade do trabalhador: "))
tempo_servico = int(input("Digite o tempo de serviço (em anos): "))

if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
    print("O trabalhador podera se aposentar.")
else:
    print("O trabalhador não podera se aposentar.")