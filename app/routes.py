# routes.py

from app import app, db
from flask import request, jsonify
from app.models import Transaction

from bson.objectid import ObjectId  # Ensure ObjectId is imported


@app.route('/test-query', methods=['GET'])
def test_query():
    try:
        transactions = Transaction.find()
        return jsonify([transaction.to_dict() for transaction in transactions])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    if request.method == 'POST':
        data = request.get_json()
        new_transaction = Transaction(
            _id=ObjectId(),
            user_id=data['user_id'],
            category=data['category'],
            amount=data['amount'],
            date=data['date'],
            timestamp=datetime.utcnow()
        )
        try:
            new_transaction.save()
            return jsonify({'message': 'Transaction added successfully'}), 201
        except Exception as e:
            logging.error(f"Error saving transaction: {e}")
            return jsonify({'message': 'Error adding transaction'}), 500
    elif request.method == 'GET':
        transactions = Transaction.find()
        return jsonify([transaction.to_dict() for transaction in transactions])

@app.route('/transactions/<string:_id>', methods=['DELETE'])
def delete_transaction(_id):
    transaction = db.transactions.find_one({'_id': ObjectId(_id)})
    if transaction:
        db.transactions.delete_one({'_id': ObjectId(_id)})
        return jsonify({'message': 'Transaction deleted successfully'}), 200
    else:
        return jsonify({'error': 'Transaction not found'}), 404
