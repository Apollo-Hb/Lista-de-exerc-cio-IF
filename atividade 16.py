###
# atividade 15
# aluno: Apollo
# Data: 08/04/2024
##Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: 𝐴 = (𝑏𝑎𝑠𝑒𝑚𝑎𝑖𝑜𝑟+𝑏𝑎𝑠𝑒𝑚𝑒𝑛𝑜𝑟∗𝑎𝑙𝑡𝑢𝑟𝑎 / 2 ,lembre-se que a base maior e a base menor devem ser números maiores que zero.

base_menor = float(input("Medida da base menor : "))
base_maior = float(input("Medida da base maior: "))
altura = float(input("Medida da altura: "))

area = ((base_maior + base_menor) * altura) / 2.0

print(f"A área do trapézio é: {area:.2f}.")