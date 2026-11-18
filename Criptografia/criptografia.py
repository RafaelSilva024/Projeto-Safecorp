import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def gerar_par_chaves():
    """Gera um par de chaves RSA (Privada e Pública)."""
    chave_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    chave_publica = chave_privada.public_key()
    return chave_privada, chave_publica

def cifrar_mensagem_hibrida(mensagem: bytes, chave_publica_rsa):
    """
    Cifra a mensagem usando AES-GCM (simétrica) e encapsula a chave AES
    usando RSA-OAEP (assimétrica).
    """
    # 1. Gerar chave simétrica de 256 bits para o AES-GCM
    chave_aes = AESGCM.generate_key(bit_length=256)
    aesgcm = AESGCM(chave_aes)
    
    # Nonce de 96 bits recomendado para AES-GCM
    nonce = os.urandom(12)
    
    # Cifrar mensagem (proporciona confidencialidade e autenticidade via tag)
    conteudo_cifrado = aesgcm.encrypt(nonce, mensagem, associated_data=None)
    
    # 2. Encapsular a chave AES usando RSA-OAEP
    chave_aes_encapsulada = chave_publica_rsa.encrypt(
        chave_aes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    return {
        "chave_aes_encapsulada": chave_aes_encapsulada,
        "nonce": nonce,
        "conteudo_cifrado": conteudo_cifrado
    }

def decifrar_mensagem_hibrida(pacote: dict, chave_privada_rsa):
    """
    Decifra a chave AES com RSA-OAEP e em seguida decifra a mensagem com AES-GCM.
    """
    # 1. Decapsular a chave AES
    chave_aes = chave_privada_rsa.decrypt(
        pacote["chave_aes_encapsulada"],
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    # 2. Decifrar a mensagem com AES-GCM
    aesgcm = AESGCM(chave_aes)
    mensagem_original = aesgcm.decrypt(pacote["nonce"], pacote["conteudo_cifrado"], associated_data=None)
    return mensagem_original
