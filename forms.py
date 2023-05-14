from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class FormBuscaLatLng(FlaskForm):
    cep = StringField('CEP', validators=[DataRequired()])
    button_submit = SubmitField('Consultar')
