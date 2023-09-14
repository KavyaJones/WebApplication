from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

class DataForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=2, max=80)])
    email = StringField('Email', [validators.Length(min=6, max=120)])
    submit = SubmitField('Submit Data')