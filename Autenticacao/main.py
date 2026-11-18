from auth import cadastrar_usuario, autenticar_usuario, banco_usuarios

def portal_login_interativo():
    print("=" * 60)
    print(" SAFECORP - PORTAL INTERATIVO DE CADASTRO E AUTENTICAÇÃO ")
    print("=" * 60)
    
    print("\n--- ETAPA 1: CADASTRO DE USUÁRIO ---")
    usuario = input("Digite o e-mail de usuário para cadastro: ").strip()
    if not usuario:
        usuario = "usuario@safecorp.com"
        print(f"Usando e-mail padrão: {usuario}")
        
    senha = input("Digite a senha do usuário: ").strip()
    if not senha:
        senha = "SenhaSegura123!"
        print(f"Usando senha padrão: {senha}")
        
    print("\nGerando Hash com Argon2id (com Salt único de 16 bytes)...")
    hash_gerada = cadastrar_usuario(usuario, senha)
    print(f"[+] Usuário cadastrado com sucesso!")
    print(f"  -> Hash Armazenada no Banco: {hash_gerada}")
    
    print("\n--- ETAPA 2: TESTE DE LOGIN INTERATIVO ---")
    user_login = input(f"Digite o e-mail para login [{usuario}]: ").strip() or usuario
    pwd_login = input("Digite a senha para autenticação: ").strip()
    
    sucesso = autenticar_usuario(user_login, pwd_login)
    
    if sucesso:
        print("\n[SUCESSO] Autenticação realizada com sucesso! Acesso concedido.")
    else:
        print("\n[NEGADO] Credenciais incorretas. Acesso negado pelo Argon2id.")

if __name__ == "__main__":
    portal_login_interativo()
