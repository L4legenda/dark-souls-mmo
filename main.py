import pygame
import pytmx
from pytmx.util_pygame import load_pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

def draw_tiled_map(tmxdata, screen):
    for layer in tmxdata.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid, in layer:
                tile = tmxdata.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * tmxdata.tilewidth, y * tmxdata.tileheight))

def rect_layer_tiled_map(tmxdata, nameLayer):
    rects = []
    layer = tmxdata.get_layer_by_name(nameLayer)
    if isinstance(layer, pytmx.TiledTileLayer):
        for x, y, gid, in layer:
            tile = tmxdata.get_tile_image_by_gid(gid)
            if tile:
                rects.append(pygame.Rect(
                    x * tmxdata.tilewidth,
                    y * tmxdata.tileheight,
                    tmxdata.tilewidth,
                    tmxdata.tileheight
                ))
    return rects

tmxdata = load_pygame("./map/map.tmx")
done = False

x = 500
y = 400

player = pygame.Rect(x, y, 50, 50)

platform = pygame.Rect(0, 700, 1000, 100)
platform2 = pygame.Rect(0, 0, 1000, 100)
platform3 = pygame.Rect(0, 0, 100, 1000)
platform4 = pygame.Rect(900, 0, 100, 1000)

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keypressed = pygame.key.get_pressed()

    if keypressed[pygame.K_w]:
        phantom_player: pygame.Rect = player.copy()
        phantom_player.y -= 2
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            player.y -= 2
    if keypressed[pygame.K_s]:
        phantom_player: pygame.Rect = player.copy()
        phantom_player.y += 2
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            player.y += 2
    if keypressed[pygame.K_a]:
        phantom_player: pygame.Rect = player.copy()
        phantom_player.x -= 2
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            player.x -= 2
    if keypressed[pygame.K_d]:
        phantom_player: pygame.Rect = player.copy()
        phantom_player.x += 2
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            player.x += 2

    screen.fill((255, 255, 255))
    draw_tiled_map(tmxdata, screen)
    pygame.draw.rect(screen, (0, 128, 255), player)
    pygame.display.flip()
    clock.tick(60)
