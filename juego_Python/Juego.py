from turtle import *
import sys 
import pygame
from Config import *


def run_game():
    # Inicializacion del juego y crear lo que es la pantalla
    pygame.init()
    crl_config = Configuraciones()
    pantalla = pygame.display.set_mode((crl_config.width, crl_config.height))
    pygame.display.set_caption('invasion alienigena')
    # Para obtener un color preciso utilizamos los colores RGB que se pueden buscar en internet
    # Iniciar el bucle principal del juego
    while True:
        # Escuchar los eventos del teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pantalla.fill(crl_config.color) # Definimos el color de la pantalla que deseamos
        # Imprime la pantalla actual
        pygame.display.flip()

run_game()
