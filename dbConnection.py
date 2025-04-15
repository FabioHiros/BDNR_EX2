from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://fabiomatsumura:123456789Fatec@mercadolivre.as8bk7j.mongodb.net/?retryWrites=true&w=majority&appName=mercadolivre"

def connect_db():
   
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.mercadolivre
    return db