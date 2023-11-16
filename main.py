import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from player import Player

player = Player()

pygame.init()

screen = pygame.display.set_mode((640, 640))

def draw_tiled_map(tmxdata, screen):
    for layer in tmxdata.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid, in layer:
                tile = tmxdata.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * tmxdata.tilewidth, y * tmxdata.tileheight))



tmxdata = load_pygame("./map/map.tmx")
done = False

x = 500
y = 400

platform = pygame.Rect(0, 700, 1000, 100)
platform2 = pygame.Rect(0, 0, 1000, 100)
platform3 = pygame.Rect(0, 0, 100, 1000)
platform4 = pygame.Rect(900, 0, 100, 1000)

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            player.stopThread()

    keypressed = pygame.key.get_pressed()

    if keypressed[pygame.K_w]:
        player.moveUp(tmxdata)
    if keypressed[pygame.K_s]:
        player.moveDown(tmxdata)
    if keypressed[pygame.K_a]:
        player.moveLeft(tmxdata)
    if keypressed[pygame.K_d]:
        player.moveRight(tmxdata)

    screen.fill((255, 255, 255))
    draw_tiled_map(tmxdata, screen)
    player.render(screen)
    pygame.display.update()
    clock.tick(60)
