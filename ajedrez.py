import pygame

# Inicializar pygame
pygame.init()

# Tamaño de la ventana
window_size = (600, 600)


# Crear ventana
screen = pygame.display.set_mode(window_size)
screen.fill((185, 185,  185))

# Título de la ventana
pygame.display.set_caption("Tablero de ajedrez")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Dibujar tablero
x, y = 0, 0
width, height = 600, 600
for row in range(8):
    for col in range(8):
        color = white if (row + col) % 2 == 0 else black
        pygame.draw.rect(screen, color, (x + col * 80, y + row * 80, 80, 80))

# Dibujar piezas
# (Aquí se pueden dibujar las piezas en las posiciones deseadas)

# Actualizar pantalla
pygame.display.flip()

# Bucle de juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Salir de pygame
pygame.quit()


