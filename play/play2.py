b = input("\nBem vindo ao herogame !!! \nOlá, você quer brincar?\nDigite sim ou nao: ")
if b == "sim":
	print("\nEba, Qual é o seu nome? ")

	nome = input()
	if nome:
		print("\n" + nome + ", qual é o seu heroi favorito? ")

	heroi = input()
	if heroi:
		print("\n" + heroi + " é o meu favorito também!  Você ganhou um bonus!\nPrefere uma armadura ou um veiculo para o seu heroi?")

	bonus = input()
	if 	bonus == "armadura":
		print("\nVoce pode escolher a habilidade(poder) que desejar.\nQual voce quer? ")
	elif bonus == "veiculo":
		print("\nQual veiculo deseja? Nave, carros, submarinos.. inclusive equipados, a escolha é sua! ")
	else:
		print("Escolha seu bonus?! ")

	final = input()
	if final:
		print("\nParabéns! você conquistou um super " + heroi + " com " + bonus + " master " + final + "!")
	else:
		print("\nEscolha seu bonus?! ")

	vilao = input("\nCuidado! você esta passando por um ambiente hostil, há muito perigo nesta área.\nAlí, um vilão! Use seu poder de ataque para combate-lo.\nQual poder de ataque deseja usar: laser ou luta ? ")
	if vilao == "laser":
		print("\nÓtima escolha, você venceu a batalha com seu " + vilao + "!\nParabéns " + nome + ". Obrigado por brincar comigo!\nTchauzinho. ") 
	elif vilao == "luta":
		print("\nÓtima escolha, você venceu a batalha na " + vilao + "!\nParabéns " + nome + ". Obrigado por brincar comigo!\nTchauzinho. ")
	else:
		print("\nTchau, obrigado por brincar comigo. ")

else:
	exit("Que pena, quem sabe uma próxima vez. Tchauzinho!!")
		