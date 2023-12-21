import pygame
from pygame import Surface, Rect
from threading import Thread
from time import sleep
from utils import rect_layer_tiled_map
from datetime import datetime, timedelta

class Player(pygame.Rect):
    sprite: Surface = None
    idle_down = []
    run_down = []
    attack_down = []

    idle_right = []
    run_right = []
    attack_right = []

    idle_up = []
    run_up = []
    attack_up = []

    run_left = []
    idle_left = []
    attack_left = []


    idle_down_index = 0
    run_down_index = 0
    attack_down_index = 0

    idle_up_index = 0
    run_up_index = 0
    attack_up_index = 0

    idle_right_index = 0
    run_right_index = 0
    attack_right_index = 0

    idle_left_index = 0
    run_left_index = 0
    attack_left_index = 0

    lifeThread = True

    move_speed = 2

    hasRenderIdle = True
    hasRenderRun = True
    hasRenderAttack = True

    state_rotation = "idle_down"

    hp = 100
    max_hp = 100

    time_attack = None

    def __init__(self):
        Rect.__init__(self, 100, 100, 32, 32)
        self.loadImage()
        self.loadSpriteIdleDown()
        self.loadSpriteRunDown()
        self.loadSpriteIdleRight()
        self.loadSpriteRunRight()
        self.loadSpriteIdleLeft()
        self.loadSpriteRunLeft()
        self.loadSpriteIdleUp()
        self.loadSpriteRunUp()

        self.loadSpriteAttackDown()
        self.loadSpriteAttackUp()
        self.loadSpriteAttackLeft()
        self.loadSpriteAttackRight()


        self.threads()

    def attack(self, hp):
        if self.time_attack:
            now = datetime.now()
            delta = now - self.time_attack
            if delta.microseconds < 150_000:
                return
        print(self.hp)
        self.hp -= hp
        self.time_attack = datetime.now()

    def loadImage(self):
        self.sprite = pygame.image.load("player.png")

    def crop(self, rect: Rect, flip=False):
        img = self.sprite.subsurface(rect)
        img = img.subsurface((9, 14, 32, 32))
        img = pygame.transform.scale(img, (self.width, self.height))
        if flip:
            img = pygame.transform.flip(img, True, False)
        return img

    def loadSpriteAttackDown(self):
        img1 = self.crop((0, 48*6, 48, 48))
        img2 = self.crop((48, 48*6, 48, 48))
        img3 = self.crop((48 * 2, 48*6, 48, 48))
        img4 = self.crop((48 * 3, 48*6, 48, 48))

        self.attack_down.append(img1)
        self.attack_down.append(img2)
        self.attack_down.append(img3)
        self.attack_down.append(img4)

    def loadSpriteAttackUp(self):
        img1 = self.crop((0, 48*8, 48, 48))
        img2 = self.crop((48, 48*8, 48, 48))
        img3 = self.crop((48 * 2, 48*8, 48, 48))
        img4 = self.crop((48 * 3, 48*8, 48, 48))

        self.attack_up.append(img1)
        self.attack_up.append(img2)
        self.attack_up.append(img3)
        self.attack_up.append(img4)

    def loadSpriteAttackRight(self):
        img1 = self.crop((0, 48*7, 48, 48))
        img2 = self.crop((48, 48*7, 48, 48))
        img3 = self.crop((48 * 2, 48*7, 48, 48))
        img4 = self.crop((48 * 3, 48*7, 48, 48))

        self.attack_right.append(img1)
        self.attack_right.append(img2)
        self.attack_right.append(img3)
        self.attack_right.append(img4)

    def loadSpriteAttackLeft(self):
        img1 = self.crop((0, 48*7, 48, 48), True)
        img2 = self.crop((48, 48*7, 48, 48), True)
        img3 = self.crop((48 * 2, 48*7, 48, 48), True)
        img4 = self.crop((48 * 3, 48*7, 48, 48), True)

        self.attack_left.append(img1)
        self.attack_left.append(img2)
        self.attack_left.append(img3)
        self.attack_left.append(img4)

    def loadSpriteIdleDown(self):
        img1 = self.crop((0, 0, 48, 48))
        img2 = self.crop((48, 0, 48, 48))
        img3 = self.crop((48 * 2, 0, 48, 48))
        img4 = self.crop((48 * 3, 0, 48, 48))
        img5 = self.crop((48 * 4, 0, 48, 48))
        img6 = self.crop((48 * 5, 0, 48, 48))
        self.idle_down.append(img1)
        self.idle_down.append(img2)
        self.idle_down.append(img3)
        self.idle_down.append(img4)
        self.idle_down.append(img5)
        self.idle_down.append(img6)

    def loadSpriteIdleRight(self):
        img1 = self.crop((0, 48, 48, 48))
        img2 = self.crop((48, 48, 48, 48))
        img3 = self.crop((48 * 2, 48, 48, 48))
        img4 = self.crop((48 * 3, 48, 48, 48))
        img5 = self.crop((48 * 4, 48, 48, 48))
        img6 = self.crop((48 * 5, 48, 48, 48))
        self.idle_right.append(img1)
        self.idle_right.append(img2)
        self.idle_right.append(img3)
        self.idle_right.append(img4)
        self.idle_right.append(img5)
        self.idle_right.append(img6)

    def loadSpriteIdleLeft(self):
        img1 = self.crop((0, 48, 48, 48), True)
        img2 = self.crop((48, 48, 48, 48), True)
        img3 = self.crop((48 * 2, 48, 48, 48), True)
        img4 = self.crop((48 * 3, 48, 48, 48), True)
        img5 = self.crop((48 * 4, 48, 48, 48), True)
        img6 = self.crop((48 * 5, 48, 48, 48), True)
        self.idle_left.append(img1)
        self.idle_left.append(img2)
        self.idle_left.append(img3)
        self.idle_left.append(img4)
        self.idle_left.append(img5)
        self.idle_left.append(img6)

    def loadSpriteRunLeft(self):
        img1 = self.crop((48 * 5, 48 * 4, 48, 48), True)
        img2 = self.crop((48 * 4, 48 * 4, 48, 48), True)
        img3 = self.crop((48 * 3, 48 * 4, 48, 48), True)
        img4 = self.crop((48 * 2, 48 * 4, 48, 48), True)
        img5 = self.crop((48, 48 * 4, 48, 48), True)
        img6 = self.crop((0, 48 * 4, 48, 48), True)
        self.run_left.append(img1)
        self.run_left.append(img2)
        self.run_left.append(img3)
        self.run_left.append(img4)
        self.run_left.append(img5)
        self.run_left.append(img6)

    def loadSpriteIdleUp(self):
        img1 = self.crop((0, 96, 48, 48))
        img2 = self.crop((48, 96, 48, 48))
        img3 = self.crop((48 * 2, 96, 48, 48))
        img4 = self.crop((48 * 3, 96, 48, 48))
        img5 = self.crop((48 * 4, 96, 48, 48))
        img6 = self.crop((48 * 5, 96, 48, 48))
        self.idle_up.append(img1)
        self.idle_up.append(img2)
        self.idle_up.append(img3)
        self.idle_up.append(img4)
        self.idle_up.append(img5)
        self.idle_up.append(img6)

    def loadSpriteRunUp(self):
        img1 = self.crop((0, 48 * 5, 48, 48))
        img2 = self.crop((48, 48 * 5, 48, 48))
        img3 = self.crop((48 * 2, 48 * 5, 48, 48))
        img4 = self.crop((48 * 3, 48 * 5, 48, 48))
        img5 = self.crop((48 * 4, 48 * 5, 48, 48))
        img6 = self.crop((48 * 5, 48 * 5, 48, 48))
        self.run_up.append(img1)
        self.run_up.append(img2)
        self.run_up.append(img3)
        self.run_up.append(img4)
        self.run_up.append(img5)
        self.run_up.append(img6)

    def loadSpriteRunDown(self):
        img1 = self.crop((0, 48 * 3, 48, 48))
        img2 = self.crop((48, 48 * 3, 48, 48))
        img3 = self.crop((48 * 2, 48 * 3, 48, 48))
        img4 = self.crop((48 * 3, 48 * 3, 48, 48))
        img5 = self.crop((48 * 4, 48 * 3, 48, 48))
        img6 = self.crop((48 * 5, 48 * 3, 48, 48))
        self.run_down.append(img1)
        self.run_down.append(img2)
        self.run_down.append(img3)
        self.run_down.append(img4)
        self.run_down.append(img5)
        self.run_down.append(img6)

    def loadSpriteRunRight(self):
        img1 = self.crop((0, 48 * 4, 48, 48))
        img2 = self.crop((48, 48 * 4, 48, 48))
        img3 = self.crop((48 * 2, 48 * 4, 48, 48))
        img4 = self.crop((48 * 3, 48 * 4, 48, 48))
        img5 = self.crop((48 * 4, 48 * 4, 48, 48))
        img6 = self.crop((48 * 5, 48 * 4, 48, 48))
        self.run_right.append(img1)
        self.run_right.append(img2)
        self.run_right.append(img3)
        self.run_right.append(img4)
        self.run_right.append(img5)
        self.run_right.append(img6)

    def render(self, screen: Surface):
        if self.state_rotation == "idle_down":
            self.animateIdleDown(screen)
        if self.state_rotation == "run_down":
            self.animateRunDown(screen)
        if self.state_rotation == "idle_right":
            self.animateIdleRight(screen)
        if self.state_rotation == "run_right":
            self.animateRunRight(screen)
        if self.state_rotation == "idle_left":
            self.animateIdleLeft(screen)
        if self.state_rotation == "run_left":
            self.animateRunLeft(screen)
        if self.state_rotation == "idle_up":
            self.animateIdleUp(screen)
        if self.state_rotation == "run_up":
            self.animateRunUp(screen)
        if self.state_rotation == "attack_down":
            self.animateAttackDown(screen)
        if self.state_rotation == "attack_up":
            self.animateAttackUp(screen)
        if self.state_rotation == "attack_right":
            self.animateAttackRight(screen)
        if self.state_rotation == "attack_left":
            self.animateAttackLeft(screen)

    def animateAttackDown(self, screen: Surface):
        if self.attack_down_index == len(self.attack_down) - 1:
            self.finishAttack()

        screen.blit(self.attack_down[self.attack_down_index], (self.x, self.y))

    def animateAttackUp(self, screen: Surface):
        if self.attack_up_index == len(self.attack_up) - 1:
            self.finishAttack()

        screen.blit(self.attack_up[self.attack_up_index], (self.x, self.y))

    def animateAttackRight(self, screen: Surface):
        if self.attack_right_index == len(self.attack_right) - 1:
            self.finishAttack()

        screen.blit(self.attack_right[self.attack_right_index], (self.x, self.y))

    def animateAttackLeft(self, screen: Surface):
        if self.attack_left_index == len(self.attack_left) - 1:
            self.finishAttack()

        screen.blit(self.attack_left[self.attack_left_index], (self.x, self.y))


    def finishAttack(self):
        self.hasRenderIdle = True
        self.hasRenderRun = True

    def animateIdleDown(self, screen: Surface):
        screen.blit(self.idle_down[self.idle_down_index], (self.x, self.y))

    def animateRunDown(self, screen: Surface):
        screen.blit(self.run_down[self.run_down_index], (self.x, self.y))

    def animateIdleRight(self, screen: Surface):
        screen.blit(self.idle_right[self.idle_right_index], (self.x, self.y))

    def animateRunRight(self, screen: Surface):
        screen.blit(self.run_right[self.run_right_index], (self.x, self.y))

    def animateIdleLeft(self, screen: Surface):
        screen.blit(self.idle_left[self.idle_left_index], (self.x, self.y))

    def animateRunLeft(self, screen: Surface):
        screen.blit(self.run_left[self.run_left_index], (self.x, self.y))

    def animateIdleUp(self, screen: Surface):
        screen.blit(self.idle_up[self.idle_up_index], (self.x, self.y))

    def animateRunUp(self, screen: Surface):
        screen.blit(self.run_up[self.run_up_index], (self.x, self.y))

    def threadMoveIndex(self):
        while self.lifeThread:
            sleep(0.125)
            # Down
            idle_down_index = self.idle_down_index
            idle_down_index += 1
            if idle_down_index >= len(self.idle_down):
                idle_down_index = 1
            self.idle_down_index = idle_down_index
            # Run Down
            run_down_index = self.run_down_index
            run_down_index += 1
            if run_down_index >= len(self.run_down):
                run_down_index = 1
            self.run_down_index = run_down_index
            # Right
            idle_right_index = self.idle_right_index
            idle_right_index += 1
            if idle_right_index >= len(self.idle_right):
                idle_right_index = 1
            self.idle_right_index = idle_right_index
            # Run Right
            run_right_index = self.run_right_index
            run_right_index += 1
            if run_right_index >= len(self.run_right):
                run_right_index = 1
            self.run_right_index = run_right_index
            # Up
            idle_up_index = self.idle_up_index
            idle_up_index += 1
            if idle_up_index >= len(self.idle_up):
                idle_up_index = 1
            self.idle_up_index = idle_up_index
            # Run Up
            run_up_index = self.run_up_index
            run_up_index += 1
            if run_up_index >= len(self.run_up):
                run_up_index = 1
            self.run_up_index = run_up_index
            # Left
            idle_left_index = self.idle_left_index
            idle_left_index += 1
            if idle_left_index >= len(self.idle_left):
                idle_left_index = 1
            self.idle_left_index = idle_left_index
            # Run Left
            run_left_index = self.run_left_index
            run_left_index += 1
            if run_left_index >= len(self.run_left):
                run_left_index = 1
            self.run_left_index = run_left_index
            # Attack Down
            attack_down_index = self.attack_down_index
            attack_down_index += 1
            if attack_down_index >= len(self.attack_down):
                attack_down_index = 1
            self.attack_down_index = attack_down_index

            # Attack Up
            attack_up_index = self.attack_up_index
            attack_up_index += 1
            if attack_up_index >= len(self.attack_up):
                attack_up_index = 1
            self.attack_up_index = attack_up_index

            # Attack Right
            attack_right_index = self.attack_right_index
            attack_right_index += 1
            if attack_right_index >= len(self.attack_right):
                attack_right_index = 1
            self.attack_right_index = attack_right_index

            # Attack Left
            attack_left_index = self.attack_left_index
            attack_left_index += 1
            if attack_left_index >= len(self.attack_left):
                attack_left_index = 1
            self.attack_left_index = attack_left_index

    def timerAttack(self):
        while self.lifeThread:
            sleep(1.5)
            if (self.state_rotation in ["idle_down", "run_down"]
                    and self.hasRenderAttack):
                self.hasRenderIdle = False
                self.hasRenderRun = False
                self.state_rotation = "attack_down"
                self.attack_down_index = 0

            if (self.state_rotation in ["idle_up", "run_up"]
                    and self.hasRenderAttack):
                self.hasRenderIdle = False
                self.hasRenderRun = False
                self.state_rotation = "attack_up"
                self.attack_up_index = 0

            if (self.state_rotation in ["idle_right", "run_right"]
                    and self.hasRenderAttack):
                self.hasRenderIdle = False
                self.hasRenderRun = False
                self.state_rotation = "attack_right"
                self.attack_right_index = 0
            if (self.state_rotation in ["idle_left", "run_left"]
                    and self.hasRenderAttack):
                self.hasRenderIdle = False
                self.hasRenderRun = False
                self.state_rotation = "attack_left"
                self.attack_left_index = 0

    def threads(self):
        t1 = Thread(target=self.threadMoveIndex)
        t1.start()

        t2 = Thread(target=self.timerAttack)
        t2.start()

    def stopThread(self):
        self.lifeThread = False

    def moveUp(self, tmxdata):
        phantom_player: pygame.Rect = self.copy()
        phantom_player.y -= self.move_speed
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            self.y -= self.move_speed
            if self.hasRenderRun:
                self.state_rotation = "run_up"

    def moveDown(self, tmxdata):
        phantom_player: pygame.Rect = self.copy()
        phantom_player.y += self.move_speed
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            self.y += self.move_speed
            if self.hasRenderRun:
                self.state_rotation = "run_down"

    def moveRight(self, tmxdata):
        phantom_player: pygame.Rect = self.copy()
        phantom_player.x += self.move_speed
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            self.x += self.move_speed
            if self.hasRenderRun:
                self.state_rotation = "run_right"

    def moveLeft(self, tmxdata):
        phantom_player: pygame.Rect = self.copy()
        phantom_player.x -= self.move_speed
        isCollide = phantom_player.collidelist(rect_layer_tiled_map(tmxdata, "Слой тайлов 2"))
        if isCollide == -1:
            self.x -= self.move_speed
            if self.hasRenderRun:
                self.state_rotation = "run_left"

    def handlerUpKeyMove(self):
        if not self.hasRenderIdle:
            return
        if self.state_rotation in ["run_up", "attack_up"]:
            self.state_rotation = "idle_up"

        if self.state_rotation in ["run_down", "attack_down"]:
            self.state_rotation = "idle_down"

        if self.state_rotation in ["run_left", "attack_left"]:
            self.state_rotation = "idle_left"

        if self.state_rotation in ["run_right", "attack_right"]:
            self.state_rotation = "idle_right"