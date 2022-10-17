from Settings import *
from Bullet import *



class Player(pygame.sprite.Sprite):
    step = 5

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img.convert()
        self.image.set_colorkey(BLACK)
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0] / 5), int(self.size[1] / 5)))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = self.step
        self.speedy = self.step
        self.shield = 100
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -self.step
        if keystate[pygame.K_s]:
            self.speedy = self.step
        if keystate[pygame.K_a]:
            self.speedx = -self.step
        if keystate[pygame.K_d]:
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

        # показать, если скрыто
        if self.hidden and (pygame.time.get_ticks() - self.hide_timer > 300000000):
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10

        # тайм-аут для бонусов
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

    def shoot(self):
        # now = pygame.time.get_ticks()
        # if now - self.last_shot > self.shoot_delay:
        #     self.last_shot = now
        if self.power == 1:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            shoot_sound.play()
        if self.power >= 2:
            bullet1 = Bullet(self.rect.left, self.rect.centery)
            bullet2 = Bullet(self.rect.right, self.rect.centery)
            all_sprites.add(bullet1)
            all_sprites.add(bullet2)
            bullets.add(bullet1)
            bullets.add(bullet2)
            shoot_sound.play()

    def hide(self):
        # временно скрыть игрока
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()