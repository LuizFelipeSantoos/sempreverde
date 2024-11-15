from models import db
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

def register_user(data):
    try:
        if User.query.filter_by(email=data['email']).first():
            return {"message": "Usuário já existe."}, 409

        password_hash = generate_password_hash(data['password'])
        user = User(name=data['name'], email=data['email'], password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        return {"message": "Usuário registrado com sucesso."}, 201
    except Exception as e:
        print(f"Erro ao registrar usuário: {e}")
        db.session.rollback()
        return {"message": "Erro ao registrar usuário."}, 500


def login_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password_hash, data['password']):
        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token, "message": "Login bem-sucedido"}, 200
    return {"message": "Credenciais inválidas"}, 401
