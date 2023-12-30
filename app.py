from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('database.db') # Conecta ao banco de dados
cursror = conn.cursor() # Cria um cursor para manipular o banco de dados

cursror.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
''') # Cria a tabela caso não exista

conn.commit() # Salva as alterações
conn.close() # Fecha a conexão

@app.route('/')
def index():
    conn = sqlite3.connect('database.db') # Conecta ao banco de dados
    cursor = conn.cursor() # Cria um cursor para manipular o banco de dados
    cursor.execute('SELECT * FROM users') # Executa o comando SQL
    users = cursor.fetchall() # Pega todos os resultados
    conn.close() # Fecha a conexão
    return render_template('index.html', users=users) # Renderiza o template