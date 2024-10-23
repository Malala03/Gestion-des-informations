import mysql.connector
from flet import *

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Remplacez par votre nom d'utilisateur MySQL
        password="",  # Remplacez par votre mot de passe MySQL
        database="infos_db"
    )

