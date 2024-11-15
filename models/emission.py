from . import db

class Emission(db.Model):
    __tablename__ = 'emissions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    km_carro = db.Column(db.Float, nullable=False)
    tipo_carro = db.Column(db.String(50), nullable=False)
    km_aviao = db.Column(db.Float, nullable=False)
    classe_voo = db.Column(db.String(50), nullable=False)
    total_co2 = db.Column(db.Float)
    num_arvores = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
