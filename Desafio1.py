print("Qual é seu nome?")
nome = input()
print("Que dia da semana é hoje?")
datetime = input()
print("Quantas calorias você ingeriu no café da manhã?")
calorias_manhã = int(input())
print("Quantas calorias você ingeriu no almoço?")
calorias_almoço = int(input())
print("Quantas calorias você ingeriu no jantar?")
calorias_jantar = int(input())
soma = calorias_manhã + calorias_almoço + calorias_jantar
print(nome + " , você ingeriu nesta " + datetime + " , " + str(soma) + " calorias")


