from random import randint
# print("Rock...")
# print("Paper...")
# print("Scissors...")

player = input("Jogador, escolha pedra, papel ou tesoura: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
	computer = "pedra"
elif rand_num == 1:
	computer = "papel"
else:
	computer = "tesoura"

print(f"computador escolheu {computer}" )

if player == computer:
	print("Empate!")
elif player == "pedra":
	if computer == "tesoura":
		print("voce venceu!")
	else:
		print("computador venceu!")
elif player == "papel":
	if computer == "pedra":
		print("voce venceu!")
	else:
		print("computador venceu!")
elif player == "tesoura":
	if computer == "papel":
		print("voce venceu!")
	else:
		print("computador venceu!")	
else:
	print("Escolha uma opção válida!")