from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb+srv://fittrack:trabalhodeaps2025@fittrack.gkwa6ir.mongodb.net/?retryWrites=true&w=majority&appName=FitTrack"
    
    client = MongoClient(CONNECTION_STRING)
    return client["FitTrack"]  # esse é o nome do banco de dados
