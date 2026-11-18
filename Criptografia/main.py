import sys
from criptografia import gerar_par_chaves, cifrar_mensagem_hibrida, decifrar_mensagem_hibrida

def menu_interativo():
    print("=" * 60)
    print(" SAFECORP - MÓDULO INTERATIVO DE CRIPTOGRAFIA HÍBRIDA ")
    print("=" * 60)
    
    print("\n[1] Gerando par de chaves RSA (2048 bits)...")
    chave_privada, chave_publica = gerar_par_chaves()
    print("[+] Chaves RSA geradas com sucesso!")
    
    # Entrada dinâmica do usuário
    texto_usuario = input("\nDigite a mensagem confidencial que deseja enviar: ").strip()
    if not texto_usuario:
        texto_usuario = "Mensagem confidencial padrão do SafeCorp Portal"
        print(f"[!] Nenhuma mensagem digitada. Usando mensagem padrão: '{texto_usuario}'")
    
    mensagem_bytes = texto_usuario.encode('utf-8')
    
    print("\n[2] Cifrando a mensagem...")
    pacote = cifrar_mensagem_hibrida(mensagem_bytes, chave_publica)
    print(f"  -> Ciphertext (Hex): {pacote['conteudo_cifrado'].hex()[:40]}...")
    print(f"  -> Chave AES Encapsulada (Hex): {pacote['chave_aes_encapsulada'].hex()[:40]}...")
    
    print("\n[3] Decifrando a mensagem com a chave privada RSA...")
    mensagem_decifrada = decifrar_mensagem_hibrida(pacote, chave_privada)
    print(f"  -> Conteúdo Decifrado: {mensagem_decifrada.decode('utf-8')}")
    
    print("\n[4] Simulação de Adulteração e Ataque de Integridade:")
    adulterar = input("Deseja simular uma adulteração no texto cifrado? (s/n): ").strip().lower()
    
    if adulterar == 's':
        conteudo_alterado = bytearray(pacote["conteudo_cifrado"])
        conteudo_alterado[0] ^= 0xFF
        pacote_adulterado = pacote.copy()
        pacote_adulterado["conteudo_cifrado"] = bytes(conteudo_alterado)
        
        print("\nAttempting decifrar pacote adulterado...")
        try:
            decifrar_mensagem_hibrida(pacote_adulterado, chave_privada)
            print("[ERRO] A adulteração não foi detectada!")
        except Exception as e:
            print(f"[SUCESSO] Falha de integridade detectada! Exceção capturada: {type(e).__name__}")
            print("  -> O algoritmo AES-GCM impediu a leitura de dados adulterados.")

if __name__ == "__main__":
    menu_interativo()
