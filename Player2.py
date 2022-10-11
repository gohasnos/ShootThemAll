from Settings import *

class Player2(pygame.sprite.Sprite):
    step = 5

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player2_img.convert()
        self.image.set_colorkey(BLACK)
        self.size = self.image.get_size()
        # create a 2x bigger image than self.image
        self.image = pygame.transform.scale(self.image, (int(self.size[0] / 5), int(self.size[1] / 5)))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = self.step
        self.speedy = self.step

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -self.step
        if keystate[pygame.K_DOWN]:
            self.speedy = self.step
        if keystate[pygame.K_LEFT]:
            self.speedx = -self.step
        if keystate[pygame.K_RIGHT]:
            self.speedx = self.step
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT