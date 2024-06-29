import sqlite3
import bcrypt

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Função para autenticar o usuário
def autenticar_usuario(email, senha):
    # Buscar as informações do usuário pelo e-mail
    cursor.execute('SELECT id, senha FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()

    # Verificar se o usuário existe no banco de dados
    if user:
        # Verificar se a senha fornecida está correta
        if bcrypt.checkpw(senha.encode('utf-8'), user[1]):
            return True
    return False

# Exemplo de autenticação de usuário
# email = 'exemplo@email.com'
# senha = 'senha123'
# if autenticar_usuario(email, senha):
#     print(f'Login bem-sucedido para o usuário com o e-mail {email}')
# else:
#     print('Credenciais inválidas')

# Fechar a conexão com o banco de dados
conn.close()