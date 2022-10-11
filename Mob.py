from random import randrange
from Settings import *


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image_orig = mob_img.convert()
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        # self.image = mob_img.convert()
        self.rect = self.image.get_rect()
        self.rect.x = randrange(WIDTH - self.rect.width)
        self.rect.y = randrange(-100, -40)
        self.speedy = randrange(1, 8)
        self.speedx = randrange(-3, 3)
        self.rot = 0
        self.rot_speed = randrange(-32, 32)
        self.last_update = pygame.time.get_ticks()
        self.image = pygame.transform.rotate(self.image, self.rot_speed)

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = randrange(WIDTH - self.rect.width)
            self.rect.y = randrange(-100, -40)
            self.speedy = randrange(1, 8)

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
