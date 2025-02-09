import time


def game():
    import pygame
    import sys
    import random
    #import self

    pygame.init()
    window = pygame.display.set_mode((0,0))

    class Player:
        def __init__(self,speed, width , height, x, y, skin, gun_skin, width_gun, height_gun, x_gun, y_gun, damage, hp):
            self.texture = pygame.image.load(skin)
            self.texture_gun = pygame.image.load(gun_skin)
            self.texture_gun = pygame.transform.scale(self.texture_gun, [width_gun, height_gun])
            self.hitbox_gun = self.texture_gun.get_rect()
            self.hitbox_gun.x = x_gun
            self.hitbox_gun.y = y_gun
            self.texture = pygame.transform.scale(self.texture, [width, height])
            self.hitbox = self.texture.get_rect()
            self.hitbox.x = x
            self.hitbox.y = y
            self.speed = speed
            self.bullets = []
            self.last_shoot = 0

        def move(self):
            keys = pygame.key.get_pressed()
            if keys [pygame.K_d]:
                self.hitbox.x += self.speed
                self.hitbox_gun.x += self.speed
            if keys [pygame.K_s]:
                self.hitbox.y += self.speed
                self.hitbox_gun.y += self.speed
            if keys [pygame.K_w]:
                self.hitbox.y -= self.speed
                self.hitbox_gun.y -= self.speed
            if keys [pygame.K_a]:
                self.hitbox.x -= self.speed
                self.hitbox_gun.x -= self.speed
            if keys[pygame.K_x]:
                if time.time()-self.last_shoot > 0.2:
                    self.bullets.append(Bullet(15,
                                               30, 10,
                                               self.hitbox.x+20, self.hitbox.y+50,
                                               "Screenshot 2025-01-26 131843.png"))
                    self.last_shoot= time.time()

            for bullet in self.bullets:
                bullet.move()

        def draw(self, window):
            window.blit(self.texture, self.hitbox)
            window.blit(self.texture_gun, self.hitbox_gun)
            for bullet in self.bullets:
                bullet.draw(window)

    class Bullet:

        def __init__(self,speed, width, height, x, y, skin):
            self.texture = pygame.image.load(skin)
            self.texture = pygame.transform.scale(self.texture, [width, height])
            self.hitbox = self.texture.get_rect()
            self.hitbox.x = x
            self.hitbox.y = y
            self.speed = speed
            self.bullets = []


        def draw(self, window):
            window.blit(self.texture, self.hitbox)


        def move(self):
            self.hitbox.x += self.speed
    class Enemy:
        def __init__(self, speed, width, height, x, y, skin, hp, damage):
            self.texture = pygame.image.load(skin)
            self.texture = pygame.transform.scale(self.texture, [width, height])
            self.hitbox = self.texture.get_rect()
            self.hitbox.x = x
            self.hitbox.y = y
            self.speed = speed
            self.bullets = []
            self.hp = hp
            self.damage = damage
        def draw(self, window):
            #pygame.draw.rect(window,[1,1,1],self.hitbox)
            window.blit(self.texture, self.hitbox)


    fps = pygame.time.Clock()

    player = Player(10, 50, 100, 650, 450, "img_2-removebg-preview.png","img_3.png", 100,70, 670,460,100,300)
    Enemy_1 = Enemy(1,300,300,400,150,'sticker-png-terraria-minecraft-boss-item-player-character-minecraft-boss-android-wiki-voodoo-doll-video-games-removebg-preview.png', 10,134)
    background = pygame.image.load('img.png')
    background = pygame.transform.scale(background, window.get_size())


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        for bullet in player.bullets:
                if bullet.hitbox.colliderect(Enemy_1.hitbox):
                    Enemy_1.hp = -10
                    player.bullets.remove(bullet)


                    break
        if Enemy_1.hp  <= 0:
            Enemy_1.hitbox.x = 5000
        Enemy_1.hitbox.x += random.randint(-50, 50)
        Enemy_1.hitbox.y += random.randint(-50, 50)
        if Enemy_1.hitbox.y > window.get_height()-Enemy_1.hitbox.height:
            Enemy_1.hitbox.y -= Enemy_1.speed

        if Enemy_1.hitbox.y <0:
            Enemy_1.hitbox.y += Enemy_1.speed


        if Enemy_1.hitbox.x > window.get_width()-Enemy_1.hitbox.width:
            Enemy_1.hitbox.x -= Enemy_1.speed

        if Enemy_1.hitbox.x <0:
            Enemy_1.hitbox.x += Enemy_1.speed


        player.move()
        if player.hitbox.y > window.get_height()-player.hitbox.height:
            player.hitbox.y -= player.speed
            player.hitbox_gun.y -= player.speed
        if player.hitbox.y <0:
            player.hitbox.y += player.speed
            player.hitbox_gun.y += player.speed

        if player.hitbox.x > window.get_width()-player.hitbox.width:
            player.hitbox.x -= player.speed
            player.hitbox_gun.x -= player.speed
        if player.hitbox.x <0:
            player.hitbox.x += player.speed
            player.hitbox_gun.x += player.speed



        window.fill([255, 255, 255])
        window.blit(background, [0, 0])
        player.draw(window)
        Enemy_1.draw(window)
        pygame.display.flip()
        fps.tick(1000)
game()