###
# atividade 10
# aluno: Apollo
# Data: 08/04/2024
##Escreva um programa que leia um número inteiro maior do que zera e devolva, na tela, a soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará com a mensagem “Número inválido”.

num = int(input("Digite um número inteiro maior do que zero: "))
if num <= 0:
    print("Número inválido")
else:
    soma = sum(int(digito) for digito in str(num))
    print(f"A soma dos algarismos é: {soma}")
