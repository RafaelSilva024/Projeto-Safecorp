import os
import sqlite3

def login_seguro(usuario, senha):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
    cursor.execute(query, (usuario, senha))
    return cursor.fetchone()

SECRET_KEY = os.getenv("SAFE_CORP_SECRET_KEY", "default_safe_key")
