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

    run_down = []
    run_up = []
    run_left = []
    run_right = []

    idle_down_index = 0
    idle_up_index = 0
    idle_right_index = 0
    idle_left_index = 0

    run_down_index = 0
    run_up_index = 0
    run_right_index = 0
    run_left_index = 0

    lifeThread = True

    move_speed = 2

    state_rotation = "idle_down"

    def __init__(self):
        Rect.__init__(self, 100, 100, 32, 32)
        self.loadImage()
        self.loadSpriteIdleDown()
        self.loadSpriteIdleRight()
        self.loadSpriteIdleLeft()
        self.loadSpriteIdleUp()
        self.loadSpriteRunDown()

        self.threads()

    def loadImage(self):
        self.sprite = pygame.image.load("player.png")

    def crop(self, rect: Rect, flip=False):
        img = self.sprite.subsurface(rect)
        img = img.subsurface((9, 14, 32, 32))
        img = pygame.transform.scale(img, (self.width, self.height))
        if flip:
            img = pygame.transform.flip(img, True, False)
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

    def loadSpriteIdleUp(self):
        size_image = 48
        img1 = self.crop((0, size_image*2, size_image, size_image))
        img2 = self.crop((size_image, size_image*2, size_image, size_image))
        img3 = self.crop((size_image*2, size_image*2, size_image, size_image))
        img4 = self.crop((size_image*3, size_image*2, size_image, size_image))
        img5 = self.crop((size_image*4, size_image*2, size_image, size_image))
        img6 = self.crop((size_image*5, size_image*2, size_image, size_image))
        self.idle_up.append(img1)
        self.idle_up.append(img2)
        self.idle_up.append(img3)
        self.idle_up.append(img4)
        self.idle_up.append(img5)
        self.idle_up.append(img6)


    def loadSpriteIdleLeft(self):
        size_image = 48
        img1 = self.crop((0, size_image, size_image, size_image), True)
        img2 = self.crop((size_image, size_image, size_image, size_image), True)
        img3 = self.crop((size_image*2, size_image, size_image, size_image), True)
        img4 = self.crop((size_image*3, size_image, size_image, size_image), True)
        img5 = self.crop((size_image*4, size_image, size_image, size_image), True)
        img6 = self.crop((size_image*5, size_image, size_image, size_image), True)
        self.idle_left.append(img1)
        self.idle_left.append(img2)
        self.idle_left.append(img3)
        self.idle_left.append(img4)
        self.idle_left.append(img5)
        self.idle_left.append(img6)

    def loadSpriteRunDown(self):
        size_image = 48
        img1 = self.crop((0, size_image*3, size_image, size_image), True)
        img2 = self.crop((size_image, size_image*3, size_image, size_image), True)
        img3 = self.crop((size_image*2, size_image*3, size_image, size_image), True)
        img4 = self.crop((size_image*3, size_image*3, size_image, size_image), True)
        img5 = self.crop((size_image*4, size_image*3, size_image, size_image), True)
        img6 = self.crop((size_image*5, size_image*3, size_image, size_image), True)
        self.run_down.append(img1)
        self.run_down.append(img2)
        self.run_down.append(img3)
        self.run_down.append(img4)
        self.run_down.append(img5)
        self.run_down.append(img6)

    def render(self, screen: Surface):
        if self.state_rotation == 'idle_down':
            self.animateIdleDown(screen)
        if self.state_rotation == 'idle_right':
            self.animateIdleRight(screen)
        if self.state_rotation == 'idle_left':
            self.animateIdleLeft(screen)
        if self.state_rotation == 'idle_up':
            self.animateIdleUp(screen)
        if self.state_rotation == 'run_down':
            self.animateRunDown(screen)

    def animateIdleDown(self, screen: Surface):
        screen.blit(self.idle_down[self.idle_down_index], (self.x, self.y))

    def animateIdleRight(self, screen: Surface):
        screen.blit(self.idle_right[self.idle_right_index], (self.x, self.y))

    def animateIdleLeft(self, screen: Surface):
        screen.blit(self.idle_left[self.idle_left_index], (self.x, self.y))

    def animateIdleUp(self, screen: Surface):
        screen.blit(self.idle_up[self.idle_up_index], (self.x, self.y))

    def animateRunDown(self, screen: Surface):
        screen.blit(self.run_down[self.run_down_index], (self.x, self.y))

    def threadMoveIndex(self):
        while self.lifeThread:
            sleep(0.1)

            # Down
            idle_down_index = self.idle_down_index
            idle_down_index += 1
            if idle_down_index >= len(self.idle_down):
                idle_down_index = 0
            self.idle_down_index = idle_down_index

            # Right
            idle_right_index = self.idle_right_index
            idle_right_index += 1
            if idle_right_index >= len(self.idle_right):
                idle_right_index = 0
            self.idle_right_index = idle_right_index

            # Up
            idle_up_index = self.idle_up_index
            idle_up_index += 1
            if idle_up_index >= len(self.idle_up):
                idle_up_index = 0
            self.idle_up_index = idle_up_index

            # Left
            idle_left_index = self.idle_left_index
            idle_left_index += 1
            if idle_left_index >= len(self.idle_left):
                idle_left_index = 0
            self.idle_left_index = idle_left_index

            # Run Down
            run_down_index = self.run_down_index
            run_down_index += 1
            if run_down_index >= len(self.run_down):
                run_down_index = 0
            self.run_down_index = run_down_index

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
            self.state_rotation = "run_up"

    def moveDown(self, tmxdata):
        phantom_player: pygame.Rect = self.copy()
        phantom_player.y += self.move_speed
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            self.y += self.move_speed
            self.state_rotation = "run_down"

    def moveRight(self, tmxdata):
        phantom_player: pygame.Rect = self.copy()
        phantom_player.x += self.move_speed
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            self.x += self.move_speed
            self.state_rotation = "run_right"

    def moveLeft(self, tmxdata):
        phantom_player: pygame.Rect = self.copy()
        phantom_player.x -= self.move_speed
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            self.x -= self.move_speed
            self.state_rotation = "run_left"

    def handlerUpKeyMove(self):
        if self.state_rotation == "run_up":
            self.state_rotation = "idle_up"

        if self.state_rotation == "run_down":
            self.state_rotation = "idle_down"

        if self.state_rotation == "run_left":
            self.state_rotation = "idle_left"

        if self.state_rotation == "run_right":
            self.state_rotation = "idle_right"