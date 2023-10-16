# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input("Insira a distância em km: "))
if distancia <= 200:
   km1 = distancia * 0.50
   print(f"O valor da sua passagem é {km1} ")
else:
   km2 = distancia * 0.45
   print(f"O valor da sua passagem é {km2}")