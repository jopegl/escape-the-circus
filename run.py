import subprocess
import sys
import os

def main():
    game_file = 'main.py'

    if not os.path.exists(game_file):
        print("Arquivo main não encontrado")
        return
    print("Iniciando o jogo...")
    try:
        subprocess.run([sys.executable, game_file], check=True)
    except subprocess.CalledProcessError as e:
        print("Ocorreu um erro ao rodar o jogo:", e)

if __name__ == '__main__':
    main()