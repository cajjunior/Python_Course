import requests
url = "https://www.spotify.com.br"

response = requests.get(url, headers={"accept": "text/plain"})

print(response.text)