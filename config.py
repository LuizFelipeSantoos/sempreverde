import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://carbon_user:sua_senha@localhost/carbon_db'
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_jwt_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
