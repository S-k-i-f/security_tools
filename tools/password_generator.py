"""
Gerador e Avaliador de Senhas: Módulo que gera senhas aleatórias fortes com ferramenta avaliadora de senhas.

O script fornece uma funcionalidade que gera senhas aleatórias
utilizando a biblioteca random (aleatoriedade) e string (força) com base
na complexidade e oferece uma ferramenta para avaliar a senha criada ou uma
existente fornecendo sugestões de melhoria
"""

import string
import random

# Definição dos caracteres: Caracteres principais que serão usados para a avalição de força das senhas.
CARACTERES_TEXTO = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
CARACTERES_NUMEROS = "0123456789"
CARACTERES_ESPECIAIS = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

# Controle de comprimento: Defini que uma senha não pode ter menos que 8 ou mais que 16 caracteres.
COMPRIMENTO_MINIMO = 8
COMPRIMENTO_MAXIMO = 16

def gerar_senha(tamanho):
    """
    Ferramenta que gera uma senha aleatória com caracteres variados.

        Características:
          • A senha aleatória combina letras maiúculas e minúsculas, números e caracteres especiais.
          • Valida o comprimento da senha antes de cria-la.
          • Gera um erro se o tmanaho for inválido e se não puder ser convertido para inteiro.
    """

    try:
        tamanho = int(tamanho)
        
        if tamanho < COMPRIMENTO_MINIMO:
            print(f"❌ A senha deve conter pelo menos {COMPRIMENTO_MINIMO} caracteres.")
            return None

        if tamanho > COMPRIMENTO_MAXIMO:
            print(f"❌ A senha deve conter no máximo {COMPRIMENTO_MAXIMO} caracteres.")

            return None

        # Combinação: Une os caracteres para que a senha atenda todos os requisitos de força.
        todos_caracteres = CARACTERES_TEXTO + CARACTERES_NUMEROS + CARACTERES_ESPECIAIS

        # Geração da senha: Gera a senha escolhendo os caracteres aleatoriamente.
        senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))

        return senha
    
    except ValueError:
        print("❌ Digite um número válido!")

        return None

def avaliar_senha(senha):
    """
    Função que avalia a força da senha e sugere melhorias.

        Características:
          • Analisa os critérios de segurança da senha (comprimento e tipos de caracteres).
          • Retorna o nível da força com feedback de para melhorias.

        Tupla de dois elementos:
          • String com os níveis de força (fraco, médio e forte).
          • Lista de sugestões de melhoria.
    """

    forca = 0
    feedback = []

    # Verificação do comprimento: verifica o comprimento mínimo.
    if len(senha) >= COMPRIMENTO_MINIMO:
        forca += 1
    else:
        feedback.append(f"Aumente sua senha para pelo menos {COMPRIMENTO_MINIMO} caracteres.")

    # Verificação de minúsculas: Verifica se tem letras minúsculas.
    if any(char in CARACTERES_TEXTO[:26] for char in senha):
        forca += 1
    else:
        feedback.append("Adicionar letras minúsculas.")

    # Vericação de letras maiúsculas: Verifica se tem letras maiúsculas.
    if any(char in CARACTERES_TEXTO[26:] for char in senha):
        forca += 1
    else:
        feedback.append("Adicioar letras maiúsculas.")

    # Verficação de números: Verifica se tem números.
    if any(char in CARACTERES_NUMEROS for char in senha):
        forca += 1
    else:
        feedback.append("Adicionar números.")

    # Verficação de especiais: Verifica se tem caracteres especiais.
    if any(char in CARACTERES_ESPECIAIS for char in senha):
        forca += 1
    else:
        feedback.append("Adicionar caracteres especiais")

    # Níveis de força: Determina o nível de força baseado na pontuação.
    if forca <= 2:
        nivel = "🔴 Fraca!"

    elif forca <= 3:
        nivel = "🟡 Pode melhorar..."

    else:
        nivel = "🟢 Forte!"
    
    return nivel, feedback

def menu_principal():
    """
    Função que exibe o menu principal e interage com o usuário.
    
    Loop que apresenta um menu com as opções de gerar uam senha, avaliar uma senha ou sair do programa.
    """

    while True:
        print("-" * 71)
        print("                        Gerador e Avaliador de Senhas")
        print("-" * 71)
        print("O que deseja fazer?")
        print("    1. Gerar uma senha aleatória")
        print("    2. Avaliar uma senha")
        print("    3. Sair")
        print("-" * 71)
        
        opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()
        
        if opcao == "1":
            gerar_senha_menu()

        elif opcao == "2":
            avaliar_senha_menu()

        elif opcao == "3":
            print("Até mais...")

            break
        else:
            print("❌ Opção inválida! Tente novamente.")

def gerar_senha_menu():
    """
    Submenu que gera a nova senha.

    Solicita ao usuário o tamanho da senha desejada, gera a senha 
    e exibe o resultado com informações sobre o comprimento.
    """

    print("-" * 71)
    print("                        Gere uma Senha Aleatória")
    print("-" * 71)
    print(f"O tamanho deve ser entre {COMPRIMENTO_MINIMO} e {COMPRIMENTO_MAXIMO} caracteres.")
    
    tamanho = input(f"Quantos caracteres você deseja? ")
    
    senha = gerar_senha(tamanho)
    
    if senha:
        print(f"✅ Sua nova senha: {senha}")
        print(f"📊 Comprimento: {len(senha)} caracteres")

def avaliar_senha_menu():
    """
    Submenu para avaliar uma senha.

    Solicita uma senha do usuário, avalia sua força e exibe
    o resultado com sugestões de melhoria se necessário.
    """
    print("-" * 71)
    print("                        Avalie sua Senha")
    print("-" * 71)
    
    senha = input("Digite ou crie uma nova senha: ")
    
    if len(senha) == 0:
        print("❌ A senha não pode estar vazia!")

        return
    
    nivel, feedback = avaliar_senha(senha)
    
    print(f"📊 Resultado: {nivel}")
    print(f"📏 Comprimento: {len(senha)} caracteres")
    
    if feedback:
        print("💡 Sugestões para melhorar:")

        for sugestao in feedback:
            print(sugestao)

    else:
        print("🎉 Sua senha é segura!")

if __name__ == "__main__":
    menu_principal()
