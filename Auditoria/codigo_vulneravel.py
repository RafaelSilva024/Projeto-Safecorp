import sqlite3

def login_inseguro(usuario, senha):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM usuarios WHERE username = '{usuario}' AND password = '{senha}'"
    cursor.execute(query)
    return cursor.fetchone()

SECRET_KEY = "minha_chave_super_secreta_123"
