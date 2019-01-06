import pygame
import random

WIDTH = 1000
HEIGHT = 1000
FPS = 80
bad_guys = 27

b = 0
act = 3
while act:
    
    rc1 = random.randint(1,225)
    rc2 = random.randint(1,225)
    rc3 = random.randint(1,225)
    b = b + 1
    if b == act:
        break
axe = (rc2, rc3, rc1)
ex = (rc3, rc1, rc2)
why = (rc1, rc2, rc3)
r = random.randrange(1,255)

new_color = (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))


BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CLR")
clock = pygame.time.Clock()



class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)# required

        self.image = pygame.Surface((30,40))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect() # fits a boundry around the image
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedx = 5
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.speedy = -5
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.speedy = 5
        self.rect.x += self.speedx
         
        self.rect.y += self.speedy

        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((40,40))
        self.image.fill(ex)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(3,7)
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(40,100)
            self.speedy = random.randrange(1,12)
            self.image.fill((random.randrange(1,255),random.randrange(1,255),random.randrange(1,255)))
            screen.fill((random.randrange(1,255),random.randrange(1,255),random.randrange(1,255)))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(r)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -20
        
    def update(self):
        self.rect.y += self.speedy
        
        if self.rect.bottom < 0:
            self.kill()

                                   

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(bad_guys):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


running = True
while running:

    

    
    
    clock.tick(FPS) # keeps loop running at the right speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # update - move jump, fire ect...

    all_sprites.update()
    mobs.update()
    

    # check to see if mob hit player

    respawn = pygame.sprite.groupcollide(mobs, bullets, True, True)# (group, group) first true is for the mobs- delets, second true is for the bullets- which deletes
    for spawn in respawn:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    hits = pygame.sprite.spritecollide(player,mobs, False) #  (sprite,group) checks if any mobs, hit player, false deletes the thing hit, like player
    if hits: # if hits has something in it, it is true which runs
        running = False

    # draw/render

    screen.fill(why)
    
    all_sprites.draw(screen)
    mobs.draw(screen)
    
    pygame.display.flip() # after drawing everything, flip the display

pygame.quit()

 
