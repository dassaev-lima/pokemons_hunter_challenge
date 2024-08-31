import pickle
import hashlib

def get_secret_password():
    # Simulação de recuperação de senha secreta (pode ser obtida de um serviço seguro ou de uma variável de ambiente)
    secret_password = os.getenv('SECRET_PASSWORD')
    if not secret_password:
        raise ValueError('SECRET_PASSWORD não configurada')
    return secret_password

def login(username, password):
    secret_password = get_secret_password()

    # Verifica se o hash da senha fornecida coincide com o hash armazenado da senha secreta
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username == 'admin' and hashed_password == secret_password:
        print('Login successful')
    else:
        print('Login failed')

if __name__ == '__main__':
    login('admin', 'secret123')
