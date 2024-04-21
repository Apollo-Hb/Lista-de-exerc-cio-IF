###
# atividade 24
# aluno: Apollo
# Data: 08/04/2024
##A tarifas de certo parque de estacionamento são as seguintes: a. 1ª e 2ª hora – R$ 1,00 cada b. 3ª e 4ª hora – R$ 1,40 cada c. 5ª hora e seguintes R$ 2,00 cada. O numero de horas a pagar é sempre inteiro arredondado por excesso. Deste modo, quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida são apresentados na foram de pares de inteiros, representando horas e minutos. Por exemplo, o par 12 50 representará “dez para a uma da tarde”. Pretendense criar um programa que, lidos pelo teclado s momento de chegada e de partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chega e a partida se dão com intervalor não superior a 24 horas. Portanto, se uma dada hora de chegada for superior à partida, isso não é uma situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada.

chegada_hora = int(input("Digite a hora de chegada (0 a 23): "))
chegada_minuto = int(input("Digite os minutos de chegada (0 a 59): "))
partida_hora = int(input("Digite a hora de partida (0 a 23): "))
partida_minuto = int(input("Digite os minutos de partida (0 a 59): "))

chegada_minutos = chegada_hora * 60 + chegada_minuto
partida_minutos = partida_hora * 60 + partida_minuto
diferenca_minutos = partida_minutos - chegada_minutos
num_horas = (diferenca_minutos + 59) // 60

if num_horas <= 2:
    preco = num_horas * 1.00
elif num_horas <= 4:
    preco = 2.00 + (num_horas - 2) * 1.40
else:
    preco = 4.80 + (num_horas - 4) * 2.00

print(f"Preço cobrado pelo estacionamento: R$ {preco:.2f}")
