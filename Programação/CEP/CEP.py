import requests

def buscar_endereco(cep):
    r = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()
    if "erro" in r:
        return "CEP não encontrado."
    return f"{r['logradouro']}, {r['bairro']}, {r['localidade']}, {r['uf']}"

print(buscar_endereco("13187074"))
