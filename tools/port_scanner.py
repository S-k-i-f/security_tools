"""
Scanner Simples de Portas TCP: Módulo de varredura de portas abertas em um host.

O scanner utiliza a biblioteca socket para criar conexões TCP e tenta
conectar a cada porta no intervalo especificado. Portas abertas são
identificadas quando a conexão é bem-sucedida.

Nota: Este script usa um timeout curto (50ms) para acelerar o processo
de varredura.
"""

import socket

# Configurações da rede: Defini o IP do alvo e a quantidade de portas que podem ser escaneadas.
ALVO = "000.000.00.00"
PORTA_INICIAL = 1
PORTA_FINAL = 1024

"""
Configurações do Scanner:

O scan começa a varredura por uma porta específica (1-1024) no host do IP.
    
        Características:
          • Itera através de todas as portas em um intervalo específico.
          • AF_INET define endereços IPv4 e SOCO_STREAM define o socket como TCP.
          • Define um timeout curto para deixar a verredura mais rápida.
"""
print(f"Escaneando o alvo: {ALVO}")
print(f"Intervalo de portas: {PORTA_INICIAL} - {PORTA_FINAL}\n")

for porta in range(PORTA_INICIAL, PORTA_FINAL + 1):

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    cliente.settimeout(0.05)

    # Tentativa de conexão: Tenta estabeler conexão com uma porta e retorna 0 para bem sucedido e outro número para falha
    if cliente.connect_ex((ALVO, porta)) == 0:
        print(f"A Porta {porta} está aberta")
    
    # Execução: Fecha o socket após cada tentativa.
    cliente.close()
print(f"\n[*] Varredura finalizada.")
