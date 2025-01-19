# __init__.py

from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
import os
import sys
import config  # Import the configuration from the root level

app = Flask(__name__)
app.config.from_object(config.Config)

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# MongoDB connection
client = MongoClient(app.config['MONGO_URI'])
db = client[app.config['MONGO_DBNAME']]

# Create the collection if it doesn't exist
if "transactions" not in db.list_collection_names():
    db.create_collection("transactions")

# Enable CORS for all routes
CORS(app)

from app import routes, models