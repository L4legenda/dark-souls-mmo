import pygame
from pygame import Surface, Rect

class Player(pygame.Rect):
    sprite: Surface = None
    idle_down = []
    idle_up = []
    idle_left = []
    idle_right = []

    def __init__(self):
        Rect.__init__(self, 0,0,32,32)
        self.loadImage()
        self.loadSpriteIdleDown()

    def loadImage(self):
        self.sprite = pygame.image.load("player.png")

    def crop(self, rect: Rect):
        return self.sprite.subsurface(rect)

    def loadSpriteIdleDown(self):
        img1 = self.crop((0, 0, 32, 32))
        img2 = self.crop((32, 0, 32, 32))
        img3 = self.crop((64, 0, 32, 32))
        img4 = self.crop((96, 0, 32, 32))
        self.idle_down.append(img1)
        self.idle_down.append(img2)
        self.idle_down.append(img3)
        self.idle_down.append(img4)

    def render(self, screen: Surface):
        screen.blit(self.idle_down[0], (self.x, self.y))