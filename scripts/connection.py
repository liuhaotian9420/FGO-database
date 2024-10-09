from pymongo import MongoClient
from sqlalchemy import create_engine

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
# Access the database
db = client['fgo']

# SQLAlchemy connection
engine_uri = 'mysql+pymysql://developer:dick920815@129.211.170.79:3306/fgo'
engine = create_engine(engine_uri)


def fetch_mongo_data(collection_name):
    # Fetch all documents in the collection
    return list(db[collection_name].find())

