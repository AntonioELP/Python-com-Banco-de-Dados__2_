from app.database import criar_tabela
from app.menu import loop_principal


def main():
    # Garante que a tabela existe antes de começar
    criar_tabela()
    # Inicia o menu no terminal
    loop_principal()


if __name__ == "__main__":
    main()
