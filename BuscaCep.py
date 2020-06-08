import requests
import json


def consultacep(cep):
    url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if url.status_code == 200:
        print('Sucesso')
    elif url.status_code == 400:
        print('Erro 400')

    endereco = url.json()

    return endereco