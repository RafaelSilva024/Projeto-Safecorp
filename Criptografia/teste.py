from criptografia import gerar_par_chaves, cifrar_mensagem_hibrida, decifrar_mensagem_hibrida

def testar_sucesso():
    print("--- Teste Automático 1: Cifragem e Decifragem ---")
    chave_privada, chave_publica = gerar_par_chaves()
    mensagem_original = b"Teste automatizado SafeCorp"
    
    pacote = cifrar_mensagem_hibrida(mensagem_original, chave_publica)
    mensagem_decifrada = decifrar_mensagem_hibrida(pacote, chave_privada)
    
    assert mensagem_original == mensagem_decifrada
    print("[SUCESSO] Mensagem decifrada perfeitamente!\n")

def testar_adulteracao():
    print("--- Teste Automático 2: Falha ao Adulterar ---")
    chave_privada, chave_publica = gerar_par_chaves()
    mensagem_original = b"Dados sensiveis corporativos"
    
    pacote = cifrar_mensagem_hibrida(mensagem_original, chave_publica)
    
    conteudo_adulterado = bytearray(pacote["conteudo_cifrado"])
    conteudo_adulterado[0] ^= 0xFF
    pacote["conteudo_cifrado"] = bytes(conteudo_adulterado)
    
    try:
        decifrar_mensagem_hibrida(pacote, chave_privada)
        print("[ERRO] A adulteracao nao foi detectada!")
    except Exception as e:
        print(f"[SUCESSO] Falha detectada como esperado! Excecao capturada: {type(e).__name__}")

if __name__ == "__main__":
    testar_sucesso()
    testar_adulteracao()
