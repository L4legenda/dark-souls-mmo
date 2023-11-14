import pygame
from pygame import Surface, Rect
from threading import Thread
from time import sleep

class Player(pygame.Rect):
    sprite: Surface = None
    idle_down = []
    idle_up = []
    idle_left = []
    idle_right = []

    idle_down_index = 0

    def __init__(self):
        Rect.__init__(self, 0,0,32,32)
        self.loadImage()
        self.loadSpriteIdleDown()
        self.threads()

    def loadImage(self):
        self.sprite = pygame.image.load("player.png")

    def crop(self, rect: Rect):
        img = self.sprite.subsurface(rect)
        img = pygame.transform.scale(img, (self.width, self.height))
        return img

    def loadSpriteIdleDown(self):
        size_image = 48
        img1 = self.crop((0, 0, size_image, size_image))
        img2 = self.crop((size_image, 0, size_image, size_image))
        img3 = self.crop((size_image*2, 0, size_image, size_image))
        img4 = self.crop((size_image*3, 0, size_image, size_image))
        self.idle_down.append(img1)
        self.idle_down.append(img2)
        self.idle_down.append(img3)
        self.idle_down.append(img4)

    def render(self, screen: Surface):
        self.animateIdleDown(screen)

    def animateIdleDown(self, screen: Surface):
        screen.blit(self.idle_down[self.idle_down_index], (self.x, self.y))


    def threadMoveIndex(self):
        while True:
            sleep(0.1)
            print(self.idle_down_index)
            self.idle_down_index += 1
            if self.idle_down_index >= len(self.idle_down):
                self.idle_down_index = 0
    def threads(self):
        t1 = Thread(target=self.threadMoveIndex)
        t1.start()



