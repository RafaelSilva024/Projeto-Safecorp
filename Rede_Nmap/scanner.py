import socket

def escanear_portas(host: str, portas: list):
    print(f"Iniciando varredura autorizada em: {host}")
    resultados = []
    
    for porta in portas:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        codigo_retorno = s.connect_ex((host, porta))
        
        status = "Aberta" if codigo_retorno == 0 else "Fechada/Filtrada"
        resultados.append((porta, status))
        s.close()
        
    return resultados

if __name__ == "__main__":
    alvo = input("Digite o IP/Host para varredura [127.0.0.1]: ").strip() or "127.0.0.1"
    portas_para_testar = [22, 80, 443, 3306, 8080]
    
    res = escanear_portas(alvo, portas_para_testar)
    print("\nResultado da Varredura:")
    for porta, status in res:
        print(f"Porta {porta}: {status}")
