# import random

# random_number = random.randint(1,10) #numbers 1 to 10
# chute = None

# while chute != random_number:
# 	chute = input("Adivinhe um numero de 1 a 10. Chuta aí: ")
# 	chute = int(chute)
# 	if chute < random_number:
# 		print("Chuta mais alto! ")
# 	elif chute > random_number: 
# 		print("Chuta mais baixo! ")
	# else:
	# 	print("Você adivinhou!")
	
# print(random_number)

#----------------- VERSAO CONTINUAR JOGANDO


import random

random_number = random.randint(1,10) #numbers 1 to 10
# chute = None (because using While True)

while True:
	chute = input("Adivinhe um numero de 1 a 10. Chuta aí: ")
	chute = int(chute)
	if chute < random_number:
		print("Chuta mais alto! ")
	elif chute > random_number: 
		print("Chuta mais baixo! ")
	else:
		print("Parabéns. Você adivinhou!")
		jogar = input("Quer jogar novamente? Digite(y/n): ")
		if jogar == "y":
			random_number = random.randint(1,10)
			chute = None
		else:
			print("Obrigado por jogar. Tchau! ")
			break


