a = 147+226
print(a)
f1 = font.SysFont(Verdana.ttf, 36)
text1 = f1.render('PYTHON is REALLY AMAZING!', True, (0, 0, 0))
rect(screen, (127, 255, 42), (10, 200, 387, 15))




trava = (127, 255, 42)
f = pygame.font.SysFont('arial', 36)
sc_text = f.render('PYTHON is REALLY AMAZING!', 1, (0, 0, 0), trava)
pos = sc_text.get_rect(center = (10, 200, 387, 15))
sc.blit(sc_text, pos)




coords = [(k + r * math.cos(2 * math.pi * i / 3), j + r * math.sin(2 * math.pi * i / 3)) for i in range(1, n + 1)]