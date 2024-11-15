from models import db
from models.emission import Emission

def calculate_emission(user_id, data):
    # Coeficientes de emissão por tipo de combustível
    coeficientes_carro = {
        "gasolina": 2.3,
        "alcool": 1.6,
        "diesel": 2.7
    }

    # Coeficientes de emissão por classe de voo
    coeficiente_basico_voo = 0.15  # Emissões em kg de CO2 por km em econômica
    coeficientes_voo = {
        "economica": coeficiente_basico_voo,
        "executiva": coeficiente_basico_voo * 1.5,
        "primeira": coeficiente_basico_voo * 2
    }

    # Calcula a emissão para o carro
    tipo_carro = data.get("tipo_carro", "gasolina")
    km_carro = data.get("km_carro", 0)
    coef_carro = coeficientes_carro.get(tipo_carro.lower(), coeficientes_carro["gasolina"])
    total_co2_carro = km_carro * coef_carro

    # Calcula a emissão para o voo
    classe_voo = data.get("classe_voo", "economica")
    km_aviao = data.get("km_aviao", 0)
    coef_voo = coeficientes_voo.get(classe_voo.lower(), coeficiente_basico_voo)
    total_co2_voo = km_aviao * coef_voo

    # Calcula a emissão total e o número de árvores necessárias para compensação
    total_co2 = total_co2_carro + total_co2_voo
    num_arvores = int(total_co2 / 20)

    # Cria e salva o registro de emissão no banco de dados
    emission = Emission(
        user_id=user_id,
        km_carro=km_carro,
        tipo_carro=tipo_carro,
        km_aviao=km_aviao,
        classe_voo=classe_voo,
        total_co2=total_co2,
        num_arvores=num_arvores
    )

    db.session.add(emission)
    db.session.commit()

    return {
        "total_co2": total_co2,
        "num_arvores": num_arvores
    }

def get_emission_history(user_id):
    # Busca o histórico de emissões para o usuário especificado
    emissions = Emission.query.filter_by(user_id=user_id).all()

    # Formata os resultados como uma lista de dicionários
    history = [
        {
            "id": emission.id,
            "km_carro": emission.km_carro,
            "tipo_carro": emission.tipo_carro,
            "km_aviao": emission.km_aviao,
            "classe_voo": emission.classe_voo,
            "total_co2": emission.total_co2,
            "num_arvores": emission.num_arvores,
            "timestamp": emission.timestamp  # Certifique-se de que o modelo Emission tenha um campo de data/hora
        }
        for emission in emissions
    ]
    return history
