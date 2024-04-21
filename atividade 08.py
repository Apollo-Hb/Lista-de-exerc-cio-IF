###
# atividade 09
# aluno: Apollo
# Data: 08/04/2024
##Faça um programa que leia 2 notas de um aluno, verifique se as notas são validas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.

nome = input("digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
    media = (nota1 + nota2) / 2
    print(f"Média: {media:.2f}")
    
    if media >= 7.0:
        if media == 10.0:
            print("Aprovado!")
        else:
            print("Reprovado!")
else:
    print("insira numeros de notas validas!")