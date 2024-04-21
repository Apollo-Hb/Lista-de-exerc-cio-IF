###
# atividade 12
# aluno: Apollo
# Data: 08/04/2024
##Faça um algoritmo que calcule a média ponderada das notas de 2 provas. A primeira prova tem peso 1 e a segunda tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual o superior a 70 pontos.

nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))

media_ponderada = (nota1 + 2 * nota2) / 3

if media_ponderada >= 70:
    notafinal = "aprovado"
else:
    notafinal = "reprovado"

print(f"A média ponderada é: {media_ponderada:.2f}")
print(f"media final do aluno: {notafinal}")