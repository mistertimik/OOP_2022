import pygame
import math
from pygame.draw import *
pygame.init()
import sys
FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
green = (0, 128, 0)
orange = (255, 102, 0)
red = (255, 42, 42)
telo = (233, 198, 175)
brown = (120, 68, 33)
eye1 = (190, 200, 183)
eye2 = (128, 179, 255)
zra = (0, 0, 0)
yellow = (255, 212, 42)
purple = (212, 42, 255)
x1 = 55
y = 360
x2 = 141
x3 = 255
x4 = 341
r = 20
n = 5
k = 3
j = 67
circle(screen, green, (100, 400), 50)
circle(screen, orange, (300, 400), 50)
line(screen, telo, (25, 220), (50, 360), 8)
line(screen, telo, (148, 360), (173, 220), 8)
line(screen, telo, (225, 220), (250, 360), 8)
line(screen, telo, (348, 360), (373, 220), 8)
circle(screen, telo, (26, 220), 10)
circle(screen, telo, (173, 220), 10)
circle(screen, telo, (226, 220), 10)
circle(screen, telo, (373, 220), 10)
polygon(screen, green, [(x1 + r * math.cos(2 * math.pi * i / n), y + r * math.sin(2 * math.pi * i / n)) for i in range(1, n+1)])
polygon(screen, green, [(x2 + r * math.cos(2 * math.pi * i / n), y + r * math.sin(2 * math.pi * i / n)) for i in range(1, n+1)])
ellipse(screen, telo, (50, 250, 100, 110))
polygon(screen, orange, [(x3 + r * math.cos(2 * math.pi * i / n), y + r * math.sin(2 * math.pi * i / n)) for i in range(1, n+1)])
polygon(screen, orange, [(x4 + r * math.cos(2 * math.pi * i / n), y + r * math.sin(2 * math.pi * i / n)) for i in range(1, n+1)])
ellipse(screen, telo, (250, 250, 100, 110))
polygon(screen, red, [(70, 320), (130, 320), (100, 350)])
polygon(screen, red, [(270, 320), (330, 320), (300, 350)])
polygon(screen, brown, [(95, 300), (105, 300), (100, 310)])
polygon(screen, brown, [(295, 300), (305, 300), (300, 310)])
circle(screen, eye1, (80, 290), 10)
circle(screen, eye1, (120, 290), 10)
circle(screen, eye2, (280, 290), 10)
circle(screen, eye2, (320, 290), 10)
circle(screen, zra, (80, 290), 3)
circle(screen, zra, (120, 290), 3)
circle(screen, zra, (280, 290), 3)
circle(screen, zra, (320, 290), 3)
coords = [(k + r * math.cos(2 * math.pi * i / 3), j + r * math.sin(2 * math.pi * i / 3)) for i in range(1, n + 1)]
polygon(screen, yellow, (coords))
trava = (127, 255, 42)
f = pygame.font.SysFont('arial', 34)
sc_text = f.render('PYTHON is REALLY AMAZING!', 1, (0, 0, 0), trava)
screen.blit(sc_text, (10, 200))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()



