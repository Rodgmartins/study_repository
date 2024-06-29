from flask import Flask, request, jsonify
from data import cadastrar_usuario
from authentication import autenticar_usuario

app = Flask(__name__)

@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    data = request.get_json()
    nome = data['nome']
    email = data['email']
    senha = data['senha']
    database.cadastrar_usuario(nome, email, senha)
    return jsonify({'mensagem': 'Usuário cadastrado com sucesso'})

@app.route('/login', methods=['POST'])
def login_usuario():
    data = request.get_json()
    email = data['email']
    senha = data['senha']
    if authentication.autenticar_usuario(email, senha):
        return jsonify({'mensagem': 'Login bem-sucedido'})
    else:
        return jsonify({'mensagem': 'Credenciais inválidas'})

if __name__ == '__main__':
    app.run(debug=True)