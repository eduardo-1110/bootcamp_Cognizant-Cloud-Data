import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
city = dados['city']
pais = dados['country']
regiao =dados['region']

print('Detalhes do Ip externo: \n')
print('IP:',ip)
print('Org:',org)
print('Cidade:',city)
print('País:',pais)
print('Regiao:',regiao)