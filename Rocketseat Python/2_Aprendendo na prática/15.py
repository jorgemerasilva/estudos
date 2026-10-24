import requests

cep = "48980000"
url = f"http://viacep.com.br/ws/{cep}/json/"
response = requests.get(url=url)

result = response.json()
print(f"{result["cep"]} {result["localidade"]} {result["estado"]} {result["uf"]}")
