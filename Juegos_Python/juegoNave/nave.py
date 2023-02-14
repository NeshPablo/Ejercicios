import pygame

class Nave():
    # Gestionamos el comportamiento de nuestra nave 

    def __init__(self, pantalla):
        self.pantalla = pantalla

        #cargamos la imagen de nuestra naver
        self.imagen = pygame.image.load('../img/SpaceShip1.bmp')
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        # Empieza cada nueva nave en la parte inferior central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom

    def blitme(self):
        #Dibuja la nave en la ubicacion actual
        self.pantalla.blit(self.imagen, self.rect)