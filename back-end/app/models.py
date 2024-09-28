from app import db

class Manifestacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(64), index=True, nullable=False)
    tipo = db.Column(db.String(64), index=True, nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    data_criacao = db.Column(db.DateTime, index=True, default=db.func.current_timestamp())


    def __init__(self, usuario, tipo, descricao):
        self.usuario = usuario
        self.tipo = tipo
        self.descricao = descricao

    def __repr__(self):
        return f'<Manifestacao {self.id} - {self.tipo}>'
    