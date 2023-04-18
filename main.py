import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((125, 125, 125))
circle(screen, (225, 225, 0), (200, 200), 100)
circle(screen, (255, 0, 0), (170, 170), 15)
circle(screen, (255, 0, 0), (230, 170), 15)
circle(screen, (0, 0, 0), (170, 170), 8)
circle(screen, (0, 0, 0), (230, 170), 8)
rect(screen, (0, 0, 0), ((150, 250), (100, 20)))
line(screen, (0, 0, 0), (210, 155), (290, 130), 10)
line(screen, (0, 0, 0), (110, 110), (190, 160), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

