import sqlite3
import bcrypt

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Criar a tabela de usuários
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT, 
                email TEXT, 
                senha TEXT)''')

# Função para cadastrar novo usuário
def cadastrar_usuario(nome, email, senha):
    # Conectar ao banco de dados SQLite
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()
        # Executar operações no banco de dados
        cursor.execute('INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))
        # Commitar as alterações
        conn.commit()

# Exemplo de cadastro de um novo usuário
# cadastrar_usuario('Exemplo', 'exemplo@email.com', 'senha123')

# Fechar a conexão com obanco de dados
conn.close()
