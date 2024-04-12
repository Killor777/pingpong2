from pygame import *

font.init()

window = display.set_mode((700, 500))

display.set_caption('Pingpong')
clock = time.Clock()

img_back = transform.scale(image.load('white_img_back.png'), (window.get_width(), window.get_height()))
img_ball = transform.scale(image.load('soccer-ball.png'), (45, 45))
img_platform = transform.scale(image.load('platform3.png'), (70, 100))

font1 = font.Font(None, 70)
score = font1.render('0', True, 'gray')




class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed=0):
        super().__init__()
        self.image = img
        self.pos_x = x
        self.pos_y = y
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def draw(self):
        window.blit(self.image, self.rect.topleft)


class Platform(GameSprite):
    def __init__(self, filename, x, y, speed):
        super().__init__(filename, x, y, speed)


    def control_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0: self.pos_y -= self.speed
        if keys[K_s] and self.rect.y < 500 - self.image.get_height(): self.pos_y += self.speed
        self.rect.y = self.pos_y

    def control_r(self):
        keys2 = key.get_pressed()
        if keys2[K_UP] and self.rect.y > 0: self.pos_y -= self.speed
        if keys2[K_DOWN] and self.rect.y < 500 - self.image.get_height(): self.pos_y += self.speed
        self.rect.y = self.pos_y


class Ball(GameSprite):
    def __init__(self, filename, x, y, speed):
        super().__init__(filename, x, y, speed)
        self.speed_x = 1
        self.speed_y = 1
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y > window.get_height() - self.rect.height or self.rect.y < 0:
            self.speed_y *= -1


        if self.rect.x > window.get_width() - self.rect.width or self.rect.x < 0:
            self.speed_x *= -1

           
           
    




platform_l = Platform(img_platform, 10, 300, 4.2)
platform_r = Platform(img_platform, 620, 100, 4.2)
ball = Ball(img_ball, 350, 250, 8)

game = True

finish = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False



    if finish == 0:        
        window.blit(img_back, (0, 0))
        platform_l.draw()
        platform_l.control_l()
        platform_r.draw()
        platform_r.control_r()
        ball.draw()
        ball.update()


        if sprite.collide_rect(ball, platform_r):
            ball.speed_x *= -1
            
        if sprite.collide_rect(ball, platform_l):
            ball.speed_x *= -1

    display.update()
    clock.tick(60)