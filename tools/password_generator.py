"""
Módulo: Gerador e Avaliador de Senhas

Este módulo gera senhas aleatórias seguras e fornece uma ferramenta
para avaliar senhas existentes.

    O que há de novo:
      • O módulo random foi substituído pela secrets, agora são gerados valores aleatórios e criptografados.
      • o módulo getpass foi adicionado para maior privacidade do usuário durante a interação com o programa.
      • Comprimento máximo aumentado para 32.
      • Novo nível na avaliação de senhas.
      • Avaliação melhorada para encorajar senhas maiores que 12 caracteres.
"""

import string
import secrets
import getpass

# Controle de comprimento: Nesta atualização, o limite máximo de caracteres agora é 32 para garantir mais segurança.
COMPRIMENTO_MINIMO = 8
COMPRIMENTO_MAXIMO = 32


def gerar_senha(tamanho):
    """
    Gera uma senha segura de comprimento usando a variável "tamanho".

        Características:
          • Valida que "tamanho" é inteiro, que atende os requisitos de comprimento
          e retorna "None" em caso de entrada inválida.
          • Garante pelo menos um caractere de cada tipo de acordo com o tamanho requisitado.
          • Utiliza algoritmos para evitar que a previsilibidade da senha.
    """

    try:
        tamanho = int(tamanho)

        if not (COMPRIMENTO_MINIMO <= tamanho <= COMPRIMENTO_MAXIMO):
            print(f"❌ O tamanho da senha deve ter entre {COMPRIMENTO_MINIMO} e {COMPRIMENTO_MAXIMO} caracteres.")

            return None

        # Categorias: define as categorias de caracteres minúsculos, maiúsculos, números e carecteres especiais.
        minusculas = string.ascii_lowercase
        maiusculas = string.ascii_uppercase
        digitos = string.digits
        especiais = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

        # Implementação das categorias: Garante que a senha tenha uma categoria de cada se houver espaço.
        caracteres = [
            secrets.choice(minusculas),
            secrets.choice(maiusculas),
            secrets.choice(digitos),
            secrets.choice(especiais)
        ]

        # Aelatoriedade: preenche o restante da senha com uma mistura de tudo e a embaralha para não ser previsível.
        categorias = minusculas + maiusculas + digitos + especiais
        tamanho_total = tamanho - len(caracteres)
        senha_restante = [secrets.choice(categorias)
                            for _ in range(tamanho_total)]

        embaralhar = caracteres + senha_restante
        secrets.SystemRandom().shuffle(embaralhar)

        return "".join(embaralhar)

    except ValueError:
        print("❌ Digite um número inteiro válido!")

        return None


def avaliar_senha(senha):
    """
    Avalia a força da senha e retorna o nivel e sugestoes de melhoria.

    Características:
      • 
    Critérios avaliados (cada um acrescenta 1 ponto):
    - Comprimento >= 12
    - Contém letras minúsculas
    - Contém letras maiúsculas
    - Contém dígitos
    - Contém caracteres especiais

    Níveis retornados (string):
    - 🔴 Inaceitável (muito curta)
    - 🔴 Fraca
    - 🟡 Média (pode ser melhorada)
    - 🟢 Forte (segura)

    Retorna:
    - nivel (str), sugestoes (list[str])
    """
    pontuacao = 0
    feedback = []

    # Critérios de avaliação
    criterios = [
        (len(senha) >= 12, "Aumentar para 12+ caracteres para maior segurança."),
        (any(c.islower() for c in senha), "Adicionar letras minúsculas."),
        (any(c.isupper() for c in senha), "Adicionar letras maiúsculas."),
        (any(c.isdigit() for c in senha), "Adicionar números."),
        (any(c in string.punctuation or c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in senha),
         "Adicionar caracteres especiais.")
    ]

    for atingido, sugestao in criterios:
        if atingido:
            pontuacao += 1
        else:
            feedback.append(sugestao)

    # Níveis de força: Nesta atualização foi criado um novo nível para maior precisão na avaliação.
    if len(senha) < COMPRIMENTO_MINIMO:
        nivel = "🔴 Inaceitável (Muito curta)"
    elif pontuacao <= 2:
        nivel = "🔴 Fraca"
    elif pontuacao <= 4:
        nivel = "🟡 Média (Pode ser melhorada)"
    else:
        nivel = "🟢 Forte (Segura)"

    return nivel, feedback

def menu_principal():
    """
    Função que exibe o menu principal interativo.
    
        Loop que apresenta um menu com as opções para:
          • Gerar uam senha.
          • Avaliar uma senha.
          • Sair do programa.
    """

    while True:
        print("-" * 71)
        print("                      Gerador e Avaliador de Senhas")
        print("-" * 71)
        print("O que deseja fazer?")
        print("    1. Gerar uma senha aleatória")
        print("    2. Avaliar uma senha")
        print("    3. Sair")
        print("-" * 71)

        opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()

        if opcao == "1":
            tamanho = input(f"Tamanho da senha ({COMPRIMENTO_MINIMO}-{COMPRIMENTO_MAXIMO}): ")
            senha = gerar_senha(tamanho)

            if senha:
                print(f"✅ Sua nova senha: {senha}")
                nivel, _ = avaliar_senha(senha)
                print(f"📊 Força: {nivel}")

        elif opcao == "2":
            senha_input = getpass.getpass("Digite ou crie uma nova senha: ")

            if not senha_input:
                print("❌ A senha nãoo pode estar vazia.")

                continue

            nivel, sugestoes = avaliar_senha(senha_input)
            print(f"📊 Resultado: {nivel}")

            if sugestoes:
                print("💡 Sugestões para melhorar:")

                for s in sugestoes:
                    print(f"    • {s}")

            else:
                print("🎉 Sua senha é segura!")

        elif opcao == "3":
            print("Até mais...")

            break

        else:
            print("❌ Opção inválida, Tente novamente.")

if __name__ == "__main__":
    menu_principal()
