"""
Captura de Pacotes

Módulo sniffer que captura e analisa pacotes de rede.

    • Permite a captura de pacotes em tempo real.
    • Exibe os endereços IP de origem e destino e o protocolo utilizado.
"""

import os
import sys
import platform
import scapy.all as scapy

def inciar_interface(interface):
    """
    Função que verfica se o usuário é administrador e se a placa está em modo promíscuo,
    caso contrário, solicita as permissões necessárias.

        • Verifica as funções de administrador.
        • Verifica se a placa de rede está em modo promíscuo.
    """

    is_admin = False

    if platform.system() == "Windows":
        import ctypes

        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

        except:
            is_admin = False

    else:
        is_admin = os.geteuid() == 0

    if not is_admin:
        print("Este script precisa ser executado como administrador (Root/Admin)!")
        sys.exit(1)

    try:
        scapy.conf.iface = interface
        scapy.conf.promisc = True
        print(f"A Interface {interface} foi configurada para modo promíscuo.")
        
    except Exception as e:
        print(f"Erro ao configurar a interface: {e}")
        sys.exit(1)

def capturar_pacotes():
    """
    Função que inicia captura os pacotes de rede.

        • Captura pacotes de várias interfaces de rede em tempo real.
    """

    print("Iniciando a captura de pacotes... Pressione Ctrl + C para parar.")
    
    try:
        scapy.sniff(prn=processar_pacote, store=False)
    
    except KeyboardInterrupt:
        print("\nCaptura de pacotes interrompida pelo usuário.")
        sys.exit(0)

def processar_pacote(pacote):
    """
    Função que processa cada pacote capturado e exibe as informações relevantes.

        • Exibe o IP de origem, IP de destino e o protocolo utilizado.
    """

    if pacote.haslayer(scapy.IP):
        
        ip_origem = pacote[scapy.IP].src
        ip_destino = pacote[scapy.IP].dst
        protocolo = pacote[scapy.IP].proto

        print(f"Pacote Capturado: {ip_origem} -> {ip_destino} | Protocolo: {protocolo}")

if __name__ == "__main__":
    print("-" * 71)
    print("Farejador de Pacotes".center(71))
    print("-" * 71)

    interface = input("Digite a interface de rede para captura: \n" \
    "\n• Rede local (wlan0) e Internet (eth0)"
    "\n• TCP (6), UDP (17), ICMP (1)")

    inciar_interface(interface)
    capturar_pacotes()
