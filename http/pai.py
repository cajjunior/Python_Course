import requests
term = input("O que deseja buscar?")
url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": term}
).json()

print(len(response["results"]))

