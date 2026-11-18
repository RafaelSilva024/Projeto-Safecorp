from auth import cadastrar_usuario, autenticar_usuario

def testar_autenticacao():
    print("--- Teste Automático de Login (Argon2id) ---")
    user = "alice@safecorp.com"
    pwd = "SenhaForteEComplexa123!"
    
    cadastrar_usuario(user, pwd)
    assert autenticar_usuario(user, pwd) is True
    assert autenticar_usuario(user, "SenhaIncorreta!") is False
    print("[SUCESSO] Testes de autenticação concluídos com êxito!")

if __name__ == "__main__":
    testar_autenticacao()
