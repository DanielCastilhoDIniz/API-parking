from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

with open('googleMapApiKey.json', 'r') as f:
    load_key = json.loads(f.read())

api_key = load_key['GOOGLE_MAPS_API_KEY']


@app.route('/api/places', methods=['GET'])
def get_nearbay_places():
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    # Verifica se as coordenadas foram fornecidas corretamente
    if not lat or not lng:
        return jsonify({'error': 'As coordenadas devem ser fornecidas.'}), 400

    # Faz a consulta do CEP para obter o endereço completo
    cep = request.args.get('cep')
    if cep:
        cep_url = f"https://cep.awesomeapi.com.br/json/{cep}"
        cep_response = requests.get(cep_url)
        endereco_dic = cep_response.json()

        if endereco_dic.get('error'):
            return jsonify({'error': endereco_dic['error']}), 400

        # Usa a cidade e o estado para refinar a busca do Google Places
        cidade = endereco_dic['city']
        estado = endereco_dic['state']
        location = f"{cidade}, {estado}"
    else:
        # Se o CEP não foi fornecido, usa a latitude e a longitude diretamente
        location = f"{lat},{lng}"
# Faz a solicitação à API do Google Places para obter os locais próximos
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius=1000&type=bar&language=pt-BR&key={api_key}"
    response = requests.get(url)
    dados = response.json()

    # Retorna os resultados em formato JSON
    return jsonify(dados), 200


if __name__ == '__main__':
    app.run(debug=True)

# # consulta CEP e localização
# cep = 58051200
# mapas = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
# endereco_dic = mapas.json()

# # coleta localização
# lat = endereco_dic['lat']
# lng = endereco_dic['lng']


# # parâmetros de busca
# radios = 1000
# type = 'bar'
# keyword = type

# url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{lng}&radius={radios}&type={type}&language=pt-BR&keyword={keyword}&key={api_key}"

# payload = {}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)
# dados = response.json()

# with open('dados.json', 'w') as f:
#     json.dump(dados, f)
