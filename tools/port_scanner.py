"""
Scanner de Portas TCP 

Módulo para varredura de portas TCP abertas em um host.

    O que há de novo:
      • Módulo threading implementado para aumentar otmização
      e a velocidade de varredura.
      • Faz uma tentativa de captura de banner (banner grabbing).
      • Número máximo de portas aumentado para 2048.
"""

import socket
import threading

# Configurações da rede: Defini o IP do alvo e a quantidade de portas que podem ser escaneadas.
IP = "000.000.00.00"
PORTA_INICIAL = 1
PORTA_FINAL = 2048

# Controle de threads: nesta atualização, o número de conexões simultâneas são limitadas para não sobrecarregar a rede.
MAX_THREADS = 100
controle = threading.Semaphore(MAX_THREADS)

def scan_porta(porta):
    """
    O scan começa a varredura por uma porta específica (1-2048) no host do IP.
    
        Características:
          • Usa timeout de 1 segundo para não travar em portas não responsivas.
          • Tenta fazer o banner grabbing se a porta estiver aberta.
          • Usa semáforo para limitar várias threads ao mesmo tempo.
    """
    with controle:

        try:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(1.0)
            
            resultado = cliente.connect_ex((IP, porta))

            if resultado == 0:
                try:
                    banner = cliente.recv(2048).decode().strip()
                    servico = f" | Serviço: {banner}" if banner else " | Serviço: Desconhecido"

                except:
                    servico = ""
                
                print(f"A Porta {porta} está aberta {servico}")
            
            cliente.close()
        except Exception:
            pass

def iniciar_scanner():
    """
    Inicia e executa a varredura das portas no intervalo configurado
    e cria uma thread para cada porta.
    """
    print("-" * 71)
    print(f"Alvo: {IP}")
    print(f"Escaneando portas {PORTA_INICIAL} até {PORTA_FINAL}...")
    print("-" * 71)

    threads = []

    # Loop para criar as threads: Uma thread só é criada quando uma anterior termina de checar uma porta.
    for porta in range(PORTA_INICIAL, PORTA_FINAL + 1):
        t = threading.Thread(target=scan_porta, args=(porta,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("-" * 71)
    print("Varredura concluída!")

if __name__ == "__main__":
    iniciar_scanner()
