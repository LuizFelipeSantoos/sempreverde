from flask import Flask
from config import Config
from models import db
from routes.auth_routes import auth_bp
from routes.emission_routes import emission_bp
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa o SQLAlchemy e JWT
db.init_app(app)
jwt = JWTManager(app)

# Registro das rotas
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(emission_bp, url_prefix='/api/emission')

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

# Rota para a URL raiz
@app.route('/')
def home():
    return "Bem-vindo à API de Redução de Pegada de Carbono!"

if __name__ == '__main__':
    app.run(debug=True)
