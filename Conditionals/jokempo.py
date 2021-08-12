# INTRO
print("\nBEM VINDO AO JOKEMPO\n")
print("...pedra...")
print("...papel...")
print ("...tesoura...\n")
print("\nJogador 1 faça sua escolha (pedra, papel ou tesoura):\n")


jogador_1 = input()
print("\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!\nNao pode olhar!!")
print("\nJogador 2 faça sua escolha (pedra, papel ou tesoura):\n")
jogador_2 = input()
if jogador_1 == "pedra" and jogador_2 == "tesoura":
	print("jogador_1 venceu!")
elif jogador_1 == "pedra" and jogador_2 == "papel":
		print("jogador_2 venceu!")
elif jogador_1 == "papel" and jogador_2 == "pedra":
		print("jogador_1 venceu!")
elif jogador_1 == "papel" and jogador_2 == "tesoura":
		print("jogador_2 venceu!")
elif jogador_1 == "tesoura" and jogador_2 == "papel":
		print("jogador_1 venceu!")
elif jogador_1 == "tesoura" and jogador_2 == "pedra":
		print("jogador_2 venceu!")
elif jogador_1 == jogador_2:
	print("\nEmpate!")		
else:
	print("\nOps! temos algum problema.\nSó valem as opções pedra, papel e tesoura.\nCuidado com erro de digitacão. ")


