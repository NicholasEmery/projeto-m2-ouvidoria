from flask import jsonify, current_app
from app import db
from app.models import Manifestacao

@current_app.route('/api/manifestacoes', methods=['GET'])
def listar_manifestacoes():
    manifestacoes = Manifestacao.query.all()
    resultado = [{"id": m.id, "usuario": m.usuario, "tipo": m.tipo, "descricao": m.descricao, "data_criacao": m.data_criacao} for m in manifestacoes]
    return jsonify(resultado)

@current_app.route('/api/manifestacao/<int:id>', methods=['GET'])
def buscar_manifestacao(id):
    manifestacao = Manifestacao.query.get_or_404(id)
    return jsonify({
        "id": manifestacao.id,
        "usuario": manifestacao.usuario,
        "tipo": manifestacao.tipo,
        "descricao": manifestacao.descricao,
        "data_criacao": manifestacao.data_criacao
    })

@current_app.route('/api/manifestacao/tipo/<string:tipo>', methods=['GET'])
def listar_por_tipo(tipo):
    manifestacoes = Manifestacao.query.filter_by(tipo=tipo).all()
    
    if not manifestacoes:
        return jsonify({"message": "Nenhuma manifestação encontrada para o tipo especificado"}), 404

    return jsonify([{
        "id": manifestacao.id,
        "usuario": manifestacao.usuario,
        "tipo": manifestacao.tipo,
        "descricao": manifestacao.descricao,
        "data_criacao": manifestacao.data_criacao
    } for manifestacao in manifestacoes])


@current_app.route('/api/manifestacao/usuario/<string:usuario>', methods=['GET'])
def listar_por_usuario(usuario):
    manifestacoes = Manifestacao.query.filter_by(usuario=usuario).all()
    
    if not manifestacoes:
        return jsonify({"message": "Nenhum usuario encontrado para o tipo especificado"}), 404

    return jsonify([{
        "id": manifestacao.id,
        "usuario": manifestacao.usuario,
        "tipo": manifestacao.tipo,
        "descricao": manifestacao.descricao,
        "data_criacao": manifestacao.data_criacao
    } for manifestacao in manifestacoes])
