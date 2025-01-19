# config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGO_URI = "mongodb+srv://matmood:123@cluster0.pup08.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    MONGO_DBNAME = "finance_manager"
