import googlemaps
import requests

API_KEY = 'AIzaSyDT2F1gK5efgeq0ysWZjfIzTG2v6fNxuiU'

#consulta CEP e localização
cep = 58051200
mapas =requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
endereco_dic = mapas.json()

#coleta localização
lat = endereco_dic['lat']
lng = endereco_dic['lng']



radios = 1000
type = 'bar'
keyword = type

url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{lng}&radius={radios}&type={type}&keyword={keyword}&key=AIzaSyDT2F1gK5efgeq0ysWZjfIzTG2v6fNxuiU"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
