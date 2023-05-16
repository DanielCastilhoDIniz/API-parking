from flask import Flask
import json
from flask import render_template, redirect, url_for, flash, request, abort

from forms import FormCep
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


app = Flask(__name__)

with open('googleMapApiKey.json', 'r') as f:
    load_key = json.loads(f.read())

api_key = load_key['GOOGLE_MAPS_API_KEY']
form_key = load_key['SECRET_KEY']

app.config['SECRET_KEY'] = form_key


@app.route('/home', methods=['GET', 'POST'])
def home():

    form = FormCep()

    if form.validate_on_submit():
        cep = form.cep.data

        return render_template('home.html', cep=cep)

    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
