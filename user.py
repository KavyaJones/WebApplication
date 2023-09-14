from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

class SignupForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm Password')
    submit = SubmitField('Sign Up')

class SigninForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Sign In')

class DataForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=2, max=80)])
    email = StringField('Email', [validators.Length(min=6, max=120)])
    submit = SubmitField('Submit Data')
