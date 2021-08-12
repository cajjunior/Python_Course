pontos1 = 0
pontos2 = 0
vitorias = 2


# INTRO
print("\nBEM VINDO AO JOKEMPO\n")

nome1 = input("Digite o nome do primeiro jogador\n")
nome2 = input("Digite o nome do segundo jogador\n")

print("...pedra...")
print("...papel...")
print ("...tesoura...\n")

print(f"\n{nome1} faça sua escolha (pedra, papel ou tesoura):\n")


while pontos1 < vitorias and pontos2 < vitorias:

	jogador_1 = input()
	print("\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!")
	print(f"\n{nome2} faça sua escolha (pedra, papel ou tesoura):\n")
	jogador_2 = input()

	if jogador_1 == "pedra" and jogador_2 == "tesoura":
		print("\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!")
		print(f"\n{nome1} venceu!")
		pontos1 += 1
	elif jogador_1 == "pedra" and jogador_2 == "papel":
		print("\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!")
		print(f"\n{nome2} venceu!")
		pontos2 += 1
	elif jogador_1 == "papel" and jogador_2 == "pedra":
		print("\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!")
		print(f"\n{nome1} venceu!")
		pontos1 += 1
	elif jogador_1 == "papel" and jogador_2 == "tesoura":
		print("\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!")
		print(f"\n{nome2} venceu!")
		pontos2 += 1
	elif jogador_1 == "tesoura" and jogador_2 == "papel":
		print(f"\n{nome1} venceu!")
		print("\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!")
		pontos1 += 1
	elif jogador_1 == "tesoura" and jogador_2 == "pedra":
		print("\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!")	
		print(f"{nome2} venceu!")
		pontos2 += 1
	elif jogador_1 == jogador_2:
		print("\nEmpate!")		
	else:
		print("\nOps! temos algum problema.\nSó valem as opções pedra, papel e tesoura.\nCuidado com erro de digitacão. ")
	
	print(f"\n{nome1} faça sua escolha (pedra, papel ou tesoura):\n")
	