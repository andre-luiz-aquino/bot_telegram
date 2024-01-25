import requests

def obter_preco_btc():
    url = "https://api.coingecko.com/api/v3/simple/price"
    parametros = {
        'ids': 'bitcoin',
        'vs_currencies': 'brl'  # Você pode alterar para 'usd', 'eur', etc., dependendo da moeda desejada
    }

    resposta = requests.get(url, params=parametros)

    if resposta.status_code == 200:
        dados = resposta.json()
        preco = dados['bitcoin']['brl']
        return preco
    else:
        print(f"Erro na solicitação. Código de status: {resposta.status_code}")
        return None

from datetime import datetime, timedelta

def obter_historico_preco_btc():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    parametros = {
        'vs_currency': 'brl',  # Você pode alterar para 'usd', 'eur', etc., dependendo da moeda desejada
        'days': '200',
        'interval': 'daily'
    }

    resposta = requests.get(url, params=parametros)

    if resposta.status_code == 200:
        dados = resposta.json()
        precos = dados['prices']
        return precos
    else:
        print(f"Erro na solicitação. Código de status: {resposta.status_code}")
        return None

def calcular_media_precos(precos):
    if not precos:
        return None

    soma_precos = sum(preco[1] for preco in precos)
    media = soma_precos / len(precos)
    return media

def encontrar_maior_preco(precos):
    if not precos:
        return None

    maior_preco = max(preco[1] for preco in precos)
    return maior_preco
    

btc = f'''
### DASHBOARD###
VAlor: {obter_preco_btc()}
Media 200: {calcular_media_precos(obter_historico_preco_btc()):.2f}
'''