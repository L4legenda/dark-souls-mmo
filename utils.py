import pygame
import pytmx

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