import pygame
import sys

FONDO= (0,0,64)
##Clases para el juego

pantalla = pygame.display.set_mode((640,480))
pygame.display.set_caption("Juego python")

reloj = pygame.time.Clock()
pygame.key.set_repeat(30)

while True:
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            sys.exit()
    pantalla.fill(FONDO)
    pygame.display.flip()