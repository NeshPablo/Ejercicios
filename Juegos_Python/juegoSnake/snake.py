import pygame
import random
import sys

# Define el tamaño de la ventana del juego
window_width = 900
window_height = 800

# Define el tamaño de los bloques del juego
block_size = 10

# Inicializa Pygame
pygame.init()

# Crea la ventana del juego
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define los colores que se utilizarán en el juego
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Crea la clase Snake que se utilizará en el juego


class Snake:
    def __init__(self):
        self.body = [[window_width/2, window_height/2]]
        self.direction = "RIGHT"

    def move(self):
        # Mueve la serpiente en la dirección actual
        if self.direction == "RIGHT":
            self.body[0][0] += block_size
        elif self.direction == "LEFT":
            self.body[0][0] -= block_size
        elif self.direction == "UP":
            self.body[0][1] -= block_size
        elif self.direction == "DOWN":
            self.body[0][1] += block_size

        # Actualiza el cuerpo de la serpiente
        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]

    def add_block(self):
        # Añade un bloque al final del cuerpo de la serpiente
        last_block = self.body[-1]
        if self.direction == "RIGHT":
            self.body.append([last_block[0]-block_size, last_block[1]])
        elif self.direction == "LEFT":
            self.body.append([last_block[0]+block_size, last_block[1]])
        elif self.direction == "UP":
            self.body.append([last_block[0], last_block[1]+block_size])
        elif self.direction == "DOWN":
            self.body.append([last_block[0], last_block[1]-block_size])

    def check_collision(self):
        # Comprueba si la serpiente ha colisionado con la pared o consigo misma
        if self.body[0][0] < 0 or self.body[0][0] >= window_width:
            return True
        elif self.body[0][1] < 0 or self.body[0][1] >= window_height:
            return True
        for i in range(1, len(self.body)):
            if self.body[0][0] == self.body[i][0] and self.body[0][1] == self.body[i][1]:
                return True
        return False

# Crea la clase Apple que se utilizará en el juego


class Apple:
    def __init__(self):
        self.x = random.randint(0, window_width/block_size-1) * block_size
        self.y = random.randint(0, window_height/block_size-1) * block_size

    def draw(self):
        # Dibuja una imagen de manzana en la ubicación de la manzana
        apple_image = pygame.image.load("./img/apple.png").convert()
        window.blit(apple_image, (self.x, self.y))


# Carga la imagen de fondo del juego
background_image = pygame.image.load("./img/background.png").convert()

# Crea la serpiente y la manzana
snake = Snake()
apple = Apple()

# Define la velocidad del juego
clock = pygame.time.Clock()
fps = 10

# Ejecuta el juego
while True:
    # Maneja los eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"

    # Mueve la serpiente y comprueba si ha colisionado con la pared o consigo misma
    snake.move()
    if snake.check_collision():
        pygame.quit()
        sys.exit()

    # Comprueba si la serpiente ha comido la manzana
    if snake.body[0][0] == apple.x and snake.body[0][1] == apple.y:
        snake.add_block()
        apple = Apple()

    # Dibuja el fondo del juego y la manzana
    window.blit(background_image, (0, 0))
    apple.draw()

    # Dibuja el cuerpo de la serpiente
    for block in snake.body:
        pygame.draw.rect(
            window, green, [block[0], block[1], block_size, block_size])

    # Actualiza la ventana del juego
    pygame.display.update()

    # Espera hasta la siguiente actualización del juego
    clock.tick(fps)
