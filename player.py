import pygame
from pygame import Surface, Rect
from threading import Thread
from time import sleep
from utils import rect_layer_tiled_map

class Player(pygame.Rect):
    sprite: Surface = None
    idle_down = []
    idle_up = []
    idle_left = []
    idle_right = []

    idle_down_index = 0
    idle_up_index = 0
    idle_right_index = 0
    idle_left_index = 0

    lifeThread = True

    move_speed = 2

    def __init__(self):
        Rect.__init__(self, 100, 100, 32, 32)
        self.loadImage()
        self.loadSpriteIdleDown()
        self.loadSpriteIdleRight()
        self.threads()

    def loadImage(self):
        self.sprite = pygame.image.load("player.png")

    def crop(self, rect: Rect):
        img = self.sprite.subsurface(rect)
        img = img.subsurface((9, 14, 32, 32))
        img = pygame.transform.scale(img, (self.width, self.height))
        return img

    def loadSpriteIdleDown(self):
        size_image = 48
        img1 = self.crop((0, 0, size_image, size_image))
        img2 = self.crop((size_image, 0, size_image, size_image))
        img3 = self.crop((size_image*2, 0, size_image, size_image))
        img4 = self.crop((size_image*3, 0, size_image, size_image))
        img5 = self.crop((size_image*4, 0, size_image, size_image))
        img6 = self.crop((size_image*5, 0, size_image, size_image))
        self.idle_down.append(img1)
        self.idle_down.append(img2)
        self.idle_down.append(img3)
        self.idle_down.append(img4)
        self.idle_down.append(img5)
        self.idle_down.append(img6)

    def loadSpriteIdleRight(self):
        size_image = 48
        img1 = self.crop((0, size_image, size_image, size_image))
        img2 = self.crop((size_image, size_image, size_image, size_image))
        img3 = self.crop((size_image*2, size_image, size_image, size_image))
        img4 = self.crop((size_image*3, size_image, size_image, size_image))
        img5 = self.crop((size_image*4, size_image, size_image, size_image))
        img6 = self.crop((size_image*5, size_image, size_image, size_image))
        self.idle_right.append(img1)
        self.idle_right.append(img2)
        self.idle_right.append(img3)
        self.idle_right.append(img4)
        self.idle_right.append(img5)
        self.idle_right.append(img6)

    def render(self, screen: Surface):
        self.animateIdleDown(screen)

    def animateIdleDown(self, screen: Surface):
        screen.blit(self.idle_down[self.idle_down_index], (self.x, self.y))

    def animateIdleRight(self, screen: Surface):
        screen.blit(self.idle_right[self.idle_right_index], (self.x, self.y))

    def threadMoveIndex(self):
        while self.lifeThread:
            sleep(0.1)
            # Down
            idle_down_index = self.idle_down_index
            idle_down_index += 1
            if idle_down_index >= len(self.idle_down):
                idle_down_index = 0
            self.idle_down_index = idle_down_index
    def threads(self):
        t1 = Thread(target=self.threadMoveIndex)
        t1.start()

    def stopThread(self):
        self.lifeThread = False

    def moveUp(self, tmxdata):
        phantom_player: pygame.Rect = self.copy()
        phantom_player.y -= self.move_speed
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            self.y -= self.move_speed

    def moveDown(self, tmxdata):
        phantom_player: pygame.Rect = self.copy()
        phantom_player.y += self.move_speed
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            self.y += self.move_speed

    def moveRight(self, tmxdata):
        phantom_player: pygame.Rect = self.copy()
        phantom_player.x += self.move_speed
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            self.x += self.move_speed
    def moveLeft(self, tmxdata):
        phantom_player: pygame.Rect = self.copy()
        phantom_player.x -= self.move_speed
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            self.x -= self.move_speed