import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("game states with mouse menu")

xpos = 0
ypos = 0
mousePos = (xpos, ypos)
mouseDown = False

state = 1
quitGame = False

while not quitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                state = 1  # Return to menu when 'q' is pressed

    if state == 1:
        button1 = 100 < mousePos[0] < 300 and 400 < mousePos[1] < 550
        button2 = 400 < mousePos[0] < 600 and 400 < mousePos[1] < 550
        button3 = 700 < mousePos[0] < 900 and 400 < mousePos[1] < 550

        if button1 and mouseDown:
            state = 2
        elif button2 and mouseDown:
            state = 3
        elif button3 and mouseDown:
            state = 4

    if state == 2:
        screen.fill((80, 200, 100))
        pygame.draw.rect(screen, (100, 230, 100), (100, 400, 200, 150))
    elif state == 3:
        screen.fill((50, 197, 200))
        pygame.draw.rect(screen, (100, 230, 100), (400, 400, 200, 150))
    elif state == 4:
        screen.fill((100, 150, 200))
        pygame.draw.rect(screen, (100, 230, 100), (700, 400, 200, 150))
    else:
        screen.fill((230, 100, 100))
        pygame.draw.rect(
            screen,
            (100, 230, 100) if not button1 else (200, 230, 200),
            (100, 400, 200, 150),
        )
        pygame.draw.rect(
            screen,
            (100, 230, 100) if not button2 else (200, 230, 200),
            (400, 400, 200, 150),
        )
        pygame.draw.rect(
            screen,
            (100, 230, 100) if not button3 else (200, 230, 200),
            (700, 400, 200, 150),
        )

    pygame.display.flip()

pygame.quit()
