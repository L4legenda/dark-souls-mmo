import pygame
from pygame import Rect, Surface
from time import sleep
from threading import Thread
from player import Player

class Mob(Rect):
    sprite = None

    idle_sprite = []
    run_sprite = []

    idle_index = 0
    run_index = 0

    lifeThread = True

    state_rotation = "idle"

    hp = 10
    move_speed = 1

    def __init__(self):
        Rect.__init__(self, 200, 300, 32, 32)
        self.loadImage()
        self.loadSpriteIdle()
        self.loadSpriteRun()
        self.threads()


    def loadImage(self):
        self.sprite = pygame.image.load("slime.png")

    def crop(self, rect: Rect, flip=False):
        img = self.sprite.subsurface(rect)
        img = pygame.transform.scale(img, (self.width, self.height))
        if flip:
            img = pygame.transform.flip(img, True, False)
        return img

    def loadSpriteIdle(self):
        img1 = self.crop((0, 0, 32, 32))
        img2 = self.crop((32, 0, 32, 32))
        img3 = self.crop((32 * 2, 0, 32, 32))
        img4 = self.crop((32 * 3, 0, 32, 32))
        self.idle_sprite.append(img1)
        self.idle_sprite.append(img2)
        self.idle_sprite.append(img3)
        self.idle_sprite.append(img4)

    def loadSpriteRun(self):
        img1 = self.crop((0, 32, 32, 32))
        img2 = self.crop((32, 32, 32, 32))
        img3 = self.crop((32 * 2, 32, 32, 32))
        img4 = self.crop((32 * 3, 32, 32, 32))
        img5 = self.crop((32 * 4, 32, 32, 32))
        img6 = self.crop((32 * 5, 32, 32, 32))
        self.run_sprite.append(img1)
        self.run_sprite.append(img2)
        self.run_sprite.append(img3)
        self.run_sprite.append(img4)
        self.run_sprite.append(img5)
        self.run_sprite.append(img6)

    def animateIdle(self, screen: Surface):
        screen.blit(self.idle_sprite[self.idle_index], (self.x, self.y))

    def animateRun(self, screen: Surface):
        screen.blit(self.run_sprite[self.run_index], (self.x, self.y))

    def render(self, screen: Surface):
        if self.state_rotation == "idle":
            self.animateIdle(screen)
        if self.state_rotation == "run":
            self.animateRun(screen)

    def threadMoveIndex(self):
        while self.lifeThread:
            sleep(0.125)
            # Idle
            idle_index = self.idle_index
            idle_index += 1
            if idle_index >= len(self.idle_sprite):
                idle_index = 1
            self.idle_index = idle_index
            # Run
            run_index = self.run_index
            run_index += 1
            if run_index >= len(self.run_sprite):
                run_index = 1
            self.run_index = run_index


    def threads(self):
        t1 = Thread(target=self.threadMoveIndex)
        t1.start()

    def stopThread(self):
        self.lifeThread = False

    def agro(self, player: Rect):
        dis = pygame.math.Vector2(self.x, self.y).distance_to((player.x, player.y))
        if dis <= 100:
            self.moveToPlayer(player)
    def moveToPlayer(self, player: Player):
        vx = 0
        vy = 0

        is_collide = self.colliderect(player)
        if is_collide:
            player.attack(4)
            return

        if self.x - player.x > 0:
            vx = -self.move_speed
        elif self.x - player.x < 0:
            vx = self.move_speed

        if self.y - player.y > 0:
            vy = -self.move_speed
        elif self.y - player.y < 0:
            vy = self.move_speed

        self.x += vx
        self.y += vy