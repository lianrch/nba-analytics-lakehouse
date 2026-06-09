from src.database.connection import engine

with engine.connect():
    print("Conexão realizada com sucesso!")