from flask import Blueprint, request, jsonify, render_template
from app.models import db, Card, Transaction

routes = Blueprint('routes', __name__)

@routes.route('/estado', methods=['GET'])
def get_cards():
    cards = Card.query.all()
    return jsonify([card.to_dict() for card in cards])

@routes.route('/estado/<int:id_tarjeta>', methods=['GET'])
def get_card(id_tarjeta):
    card = Card.query.get_or_404(id_tarjeta)
    return jsonify(card.to_dict())

@routes.route('/estado', methods=['POST'])
def create_card():
    data = request.get_json()
    new_card = Card(**data)
    db.session.add(new_card)
    db.session.commit()
    return jsonify(new_card.to_dict()), 201

@routes.route('/estado/<int:id_tarjeta>', methods=['PUT'])
def update_card(id_tarjeta):
    data = request.get_json()
    card = Card.query.get_or_404(id_tarjeta)
    for key, value in data.items():
        setattr(card, key, value)
    db.session.commit()
    return jsonify(card.to_dict())

@routes.route('/cards/<int:id_tarjeta>', methods=['DELETE'])
def delete_card(id_tarjeta):
    card = Card.query.get_or_404(id_tarjeta)
    db.session.delete(card)
    db.session.commit()
    return '', 204

@routes.route('/transaccion', methods=['POST'])
def create_transaction():
    data = request.get_json()
    new_transaction = Transaction(**data)
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify(new_transaction.to_dict()), 201

@routes.route('/transaccion/<int:id_transaccion>', methods=['GET'])
def get_transaction(id_transaccion):
    transaction = Transaction.query.get_or_404(id_transaccion)
    return jsonify(transaction.to_dict())

@routes.route('/transaccion', methods=['GET'])
def get_transaccion():
    transaccion = Transaction.query.all()
    return jsonify([transaction.to_dict() for transaction in transaccion])

@routes.route('/estado', methods=['GET'])
def estado_page():
    return render_template('estado.html')

@routes.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@routes.route('/menu', methods=['GET'])
def menu_page():
    return render_template('menu.html')

@routes.route('/recarga', methods=['GET'])
def recarga_page():
    return render_template('recarga.html')