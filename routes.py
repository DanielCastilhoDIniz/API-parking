from flask import Flask, render_template, request, redirect
import json
import requests
from forms import FormCep
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

with open('googleMapApiKey.json', 'r') as f:
    load_key = json.loads(f.read())

api_key = load_key['GOOGLE_MAPS_API_KEY']
form_key = load_key['SECRET_KEY']

app.config['SECRET_KEY'] = form_key


@app.route('/home', methods=['GET', 'POST'])
def home():
    form = FormCep()

    if form.validate_on_submit() and 'button_submit' in request.form:
        cep = form.cep.data
        cep_url = f"https://cep.awesomeapi.com.br/json/{cep}"
        cep_response = requests.get(cep_url)
        endereco_dic = cep_response.json()
        lat = endereco_dic['lat']
        lng = endereco_dic['lng']
        coordenadas = [(lat, lng)]
        

        return render_template('home.html', form=form, cep=cep, lat=lat, lng=lng, coordenadas=coordenadas, api_key=api_key)

    return render_template('home.html', form=form)


@app.route('/resposta', methods=['GET'])
def resposta():
    return render_template('resposta.html')

if __name__ == '__main__':
    app.run(debug=True)
