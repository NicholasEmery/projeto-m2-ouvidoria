from flask import request, jsonify, current_app
from app import db
from app.models import Manifestacao

@current_app.route('/api/manifestacao/<int:id>', methods=['PUT'])
def atualizar_manifestacao(id):
    manifestacao = Manifestacao.query.get_or_404(id)
    dados = request.get_json()

    manifestacao.usuario = dados.get('usuario', manifestacao.usuario)
    manifestacao.tipo = dados.get('tipo', manifestacao.tipo)
    manifestacao.descricao = dados.get('descricao', manifestacao.descricao)

    db.session.commit()
    return jsonify({"mensagem": "Manifestação atualizada com sucesso"})


@current_app.route('/api/deletar/manifestacao/<int:id>', methods=['DELETE'])
def excluir_manifestacao(id):
    manifestacao = Manifestacao.query.get_or_404(id)
    db.session.delete(manifestacao)
    db.session.commit()

    return jsonify({"mensagem": "Manifestação excluída com sucesso"})