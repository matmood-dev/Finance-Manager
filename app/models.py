# models.py

from datetime import datetime
from pymongo import MongoClient
from flask_pymongo import PyMongo
from bson.objectid import ObjectId  # Ensure ObjectId is imported

client = MongoClient("mongodb+srv://matmood:123@cluster0.pup08.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["finance_manager"]

class Transaction:
    def __init__(self, _id, user_id, category, amount, date, timestamp):
        self._id = str(_id)
        self.user_id = user_id
        self.category = category
        self.amount = amount
        self.date = date
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "_id": self._id,
            'user_id': self.user_id,
            'category': self.category,
            'amount': self.amount,
            'date': self.date,
            'timestamp': self.timestamp
        }

    @classmethod
    def find(cls):
        return [cls(**transaction) for transaction in db.transactions.find()]

    def save(self):
        db.transactions.insert_one(self.to_dict())

    def delete(self):
        db.transactions.delete_one({'_id': ObjectId(self._id)})
