import os
import pygame

WIDTH = 1280  # ширина игрового окна
HEIGHT = 800  # высота игрового окна
FPS = 120
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
mob_number = 8

pygame.init()
pygame.mixer.init()  # для звука

# настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
snd_folder = os.path.join(game_folder, 'snd')

# Загрузка всей игровой графики и музыки

#ЗВУКИ
shoot_sound = pygame.mixer.Sound(os.path.join(snd_folder, 'pew.wav'))
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(os.path.join(snd_folder, snd)))
death_sound = pygame.mixer.Sound(os.path.join(snd_folder, 'expl1.wav'))
player_hit_sound = pygame.mixer.Sound(os.path.join(snd_folder, 'expl2.wav'))
pygame.mixer.music.load(os.path.join(snd_folder, 'tgfcoder-FrozenJam-SeamlessLoop.mp3'))
pygame.mixer.music.set_volume(0.4)

#СПРАЙТЫ
background = pygame.image.load(os.path.join(img_folder, 'space1.png'))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()

player_img = pygame.image.load(os.path.join(img_folder, 'ship5.png'))
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)

player2_img = pygame.image.load(os.path.join(img_folder, 'ship1.png'))
mob_img = pygame.image.load(os.path.join(img_folder, 'laserRed12.png'))

bullet_img = pygame.image.load(os.path.join(img_folder, 'laserGreen09.png'))

powerup_images = {'shield': pygame.image.load(os.path.join(img_folder, 'shield_gold.png')),
                  'gun': pygame.image.load(os.path.join(img_folder, 'bolt_gold.png'))}

explosion_anim = {'lg': [], 'sm': [], 'player': []}

for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(os.path.join(img_folder, filename))
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(os.path.join(img_folder, filename))
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
mobs = pygame.sprite.Group()