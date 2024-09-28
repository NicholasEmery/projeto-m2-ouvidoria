from flask import request, jsonify, current_app
from app import db
from app.models import Manifestacao

@current_app.route('/api/manifestacao', methods=['POST'])
def criar_manifestacao():
    dados = request.get_json()
    usuario = dados.get('usuario')
    tipo = dados.get('tipo')
    descricao = dados.get('descricao')

    if not tipo or not descricao:
        return jsonify({"erro": "Tipo e descrição são obrigatórios"}), 400

    manifestacao = Manifestacao(usuario=usuario,tipo=tipo, descricao=descricao)
    db.session.add(manifestacao)
    db.session.commit()

    return jsonify({"mensagem": "Manifestação criada com sucesso", "id": manifestacao.id}), 201