###
# atividade 15
# aluno: Apollo
# Data: 08/04/2024
##Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%.; RJ 15%; MS 8%). Faça um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado não for valido, mostrar uma mensagem de erro.

impostos = {
    "MG": 0.07,
    "SP": 0.12,
    "RJ": 0.15,
    "MS": 0.08
}

valor_produto = float(input("Digite o valor do produto: "))
estado_destino = input("Digite a sigla do estado de destino (MG, SP, RJ ou MS):")

if estado_destino == "MG":
    imposto = impostos["MG"]
    preco_final = valor_produto * (1 + imposto)
    print(f"Preço final do produto no estado MG: R$ {preco_final:.2f}")
elif estado_destino == "SP":
    imposto = impostos["SP"]
    preco_final = valor_produto * (1 + imposto)
    print(f"Preço final do produto no estado SP: R$ {preco_final:.2f}")
elif estado_destino == "RJ":
    imposto = impostos["RJ"]
    preco_final = valor_produto * (1 + imposto)
    print(f"Preço final do produto no estado RJ: R$ {preco_final:.2f}")
elif estado_destino == "MS":
    imposto = impostos["MS"]
    preco_final = valor_produto * (1 + imposto)
    print(f"Preço final do produto no estado MS: R$ {preco_final:.2f}")
else:
    print("Estado inválido. Digite uma sigla válida (MG, SP, RJ ou MS).")