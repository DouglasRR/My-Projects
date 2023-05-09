# Módulos
import random
from os import system, name

# Funções

def limpar_tela(): # Limpar terminal

    # Windows
    if name == "nt":
        _ = system("cls")
    
    # MAC ou LINUX
    else:
        _ = system("clear")

def game():

    limpar_tela()

    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de Palavras para o jogo
    palavras = ["banana", "uva", "abacate", "abacaxi", "maça"]

    # Escolhe aleatóriamente uma palavra na lista de palavras