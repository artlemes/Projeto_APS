import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Carrega as variáveis do arquivo .env
load_dotenv()

def get_database():
    CONNECTION_STRING = os.getenv("MONGODB_URI")
    
    if not CONNECTION_STRING:
        raise ValueError("CONNECTION_STRING não encontrada no .env")

    client = MongoClient(CONNECTION_STRING)
    return client["FitTrack"]

def users_collection():
    db = get_database()
    return db["users"]

def workout_plans_collection():
    db = get_database()
    return db["workout_plans"]
