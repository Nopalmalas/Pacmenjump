# Persiapan File dan Aset-aset
from pygame import*
from random import choice
LEBAR = 700
TINGGI = 500
window = display.set_mode((LEBAR, TINGGI))
display.set_caption("Nama Game Kalian")

bg = transform.scale(image.load('bg.png'), (LEBAR, TINGGI))
gravitasi = 0.9

#Class
class GameSprite(sprite.Sprite):
  def __init__(self, img, x, y, w, h):
      super().__init__()
      self.image = transform.scale(image.load(img), (w, h))  
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y

  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, img, x, y, w, h):
        super().__init__(img, x, y, w, h)
        self.vel_y = 0
        self.on_ground = False
        self.jump_power = 15

    def update(self):
        keys = key.get_pressed()
        if keys [K_SPACE] and self.on_ground:
            self.vel_y = -self.jump_power
            self.on_ground = False

        self.vel_y += gravitasi
        self.rect.y += self.vel_y
        print(self.vel_y)

        if self.rect.bottom >= 450:
            self.on_ground = True
            self.vel_y = 0
            self.rect.bottom = 450

class Enemy(GameSprite):
    def __init__(self, img, x, y, w, h):
        super().__init__(img, x, y, w, h)

    def update(self):
        self.rect.x -= 6
        if self.rect.x < -50:
            self.rect.x = 800

#buat objek
player = Player('mc.png', 100, 200, 50, 50)
enemy1 = Enemy('musuh1.png', 600, 400, 50, 50)
enemy2 = Enemy('musuh2.png', 0, 320, 50, 50)

#Score
skor = 0

font.init()
font1 = font.SysFont('Arial', 36)
papan_skor = font1.render(f'Score: {skor}', True, (255, 255, 255))
pesan_mengulang = font1.render("You lost, want to try again?(press space)", True, (255, 255, 255))

#FPS
clock = time.Clock()
FPS = 60

stop = False
# Loop Game
run = True
while run:
    clock.tick(FPS)

    # Mendeteksi Event
    for e in event.get():
        if e.type == QUIT:
            run = False
    # Meletakkan Aset dan Objek
    if stop == False:
        skor += 0.1
        papan_skor = font1.render(f'Score: {skor}', True, (255, 255, 255))

        if sprite.collide_rect(player, enemy1):
            stop = True
        if sprite.collide_rect(player, enemy2):
            stop = True
        window.blit(bg, (0, 0))
        player.reset()
        player.update()
        enemy1.reset()
        enemy1.update()
        enemy2.reset()
        enemy2.update()
        window.blit(papan_skor, (10, 10))
    if stop == True:
        window.blit(pesan_mengulang, (100, 100))
        keys = key.get_pressed()
        if keys[K_SPACE]:
            skor = 0
            stop = False
            enemy1.rect.x = 800

    display.update()
