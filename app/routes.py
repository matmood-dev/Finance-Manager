from app import app, db
from flask import request, jsonify
from app.models import Transaction

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.order_by(Transaction.timestamp.desc()).all()
    transactions_list = [{'id': t.id, 'user_id': t.user_id, 'category': t.category, 'amount': t.amount, 'date': t.date, 'timestamp': t.timestamp} for t in transactions]
    return jsonify(transactions_list)

@app.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.get_json()
    new_transaction = Transaction(
        user_id=data['user_id'],
        category=data['category'],
        amount=data['amount'],
        date=data['date']
    )
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction added successfully'}), 201

@app.route('/transactions/<int:id>', methods=['DELETE'])
def delete_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    db.session.delete(transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction deleted successfully'}), 200
