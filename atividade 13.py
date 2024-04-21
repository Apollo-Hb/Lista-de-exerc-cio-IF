###
# atividade 13
# aluno: Apollo
# Data: 08/04/2024
##A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliaçãosemestral e a um exame final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.

nota_semestre = float(input("Digite a nota da avaliação semestral (entre 0 e 10): "))
nota_exame = float(input("Digite a nota do exame final (entre 0 e 10): "))
nota_laboratorio = float(input("Digite a nota do trabalho de laboratório (entre 0 e 10): "))

media_ponderada = (2 * nota_laboratorio + 3 * nota_semestre + 5 * nota_exame) / 10

if media_ponderada < 3:
    notafinal = "reprovado"
elif media_ponderada < 5:
    notafinal = "em recuperação"
else:
    notafinal = "aprovado"

print(f"A média ponderada é: {media_ponderada:.2f}")
print(f"Situação do aluno: {notafinal}")