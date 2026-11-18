from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher(
    time_cost=3,        # Número de iterações
    memory_cost=65536,  # 64MB
    parallelism=4,      # 4 threads
    hash_len=32,        # Tamanho da hash
    salt_len=16         # Tamanho do salt
)

banco_usuarios = {}

def cadastrar_usuario(usuario: str, senha_texto_puro: str):
    """Cadastra usuário armazenando a hash gerada pelo Argon2id (com salt automático)."""
    hash_senha = ph.hash(senha_texto_puro)
    banco_usuarios[usuario] = hash_senha
    return hash_senha

def autenticar_usuario(usuario: str, senha_texto_puro: str) -> bool:
    """Verifica credenciais garantindo comparação segura."""
    if usuario not in banco_usuarios:
        return False
    
    hash_armazenada = banco_usuarios[usuario]
    try:
        return ph.verify(hash_armazenada, senha_texto_puro)
    except VerifyMismatchError:
        return False
