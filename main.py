
def game():
    import pygame
    import sys
    import random
    #import self

    pygame.init()
    window = pygame.display.set_mode((0,0))

    class Player:
        def __init__(self,speed, width , height, x, y, skin, gun_skin, width_gun, height_gun, x_gun, y_gun):
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
        def draw(self, window):
            window.blit(self.texture, self.hitbox)
            window.blit(self.texture_gun, self.hitbox_gun)
            for bullet in self.bullets:
                bullet.draw(window)


    fps = pygame.time.Clock()
    player = Player(10, 50, 100, 650, 450, "img_2-removebg-preview.png","img_3.png", 50,50, 680,480)
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
        player.move()
        window.fill([255, 255, 255])
        window.blit(background, [0, 0])
        player.draw(window)
        pygame.display.flip()
        fps.tick(144)
game()