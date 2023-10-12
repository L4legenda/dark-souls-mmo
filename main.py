import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 800))
done = False

x = 0
y = 0

player = pygame.Rect(x, y, 50, 50)

platform = pygame.Rect(0, 700, 1000, 100)

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keypressed = pygame.key.get_pressed()

    if keypressed[pygame.K_w]:
        phantom_player: pygame.Rect = player.copy()
        phantom_player.y -= 2
        isCollide = phantom_player.colliderect(platform)
        if not isCollide:
            player.y -= 2
    if keypressed[pygame.K_s]:
        phantom_player: pygame.Rect = player.copy()
        phantom_player.y += 2
        isCollide = phantom_player.colliderect(platform)
        if not isCollide:
            player.y += 2
    if keypressed[pygame.K_a]:
        phantom_player: pygame.Rect = player.copy()
        phantom_player.x -= 2
        isCollide = phantom_player.colliderect(platform)
        if not isCollide:
            player.x -= 2
    if keypressed[pygame.K_d]:
        phantom_player: pygame.Rect = player.copy()
        phantom_player.x += 2
        isCollide = phantom_player.collidelist(platform)
        if not isCollide:
            player.x += 2

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 128, 255), player)
    pygame.display.flip()
    clock.tick(60)
