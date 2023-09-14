from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

class SigninForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Sign In')
