import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 800))
done = False

isMoveRight = True
x = 0

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if isMoveRight:
        x += 1
    else:
        x -= 1
    if x == 0:
        isMoveRight = True
    if x == 740:
        isMoveRight = False

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, 30, 60, 60))
    pygame.display.flip()
    clock.tick(60)