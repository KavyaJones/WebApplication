from flask_sqlalchemy import SQLAlchemy

sqlalchemy_instance = SQLAlchemy()

class UserData(sqlalchemy_instance.Model):
    id = sqlalchemy_instance.Column(sqlalchemy_instance.Integer, primary_key=True)
    user_id = sqlalchemy_instance.Column(sqlalchemy_instance.Integer, sqlalchemy_instance.ForeignKey('user.id'), nullable=False)
    name = sqlalchemy_instance.Column(sqlalchemy_instance.String(80), nullable=False)
    email = sqlalchemy_instance.Column(sqlalchemy_instance.String(120), nullable=False)
    user = sqlalchemy_instance.relationship('User', back_populates='user_data')
