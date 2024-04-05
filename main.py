from pygame import *


window = display.set_mode((700, 500))

display.set_caption('Pingpong')


img_back = transform.scale(image.load('white_img_back.png'), (window.get_width(), window.get_height()))
img_ball = transform.scale(image.load('ball.png'), (60, 60))
img_platform = transform.scale(image.load('platform.png'), (20, 100))



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

    def control(self):
        keys = key.get_pressed()
        if keys[K_w]: self.pos_y += self.speed
        if keys[K_s]: self.pos_y -= self.speed

class Platform2(GameSprite):
    def __init__(self, filename, x, y, speed):
        super().__init__(filename, x, y, speed)

    def control(self):
        keys = key.get_pressed()
        #TODO add control for second platform



class Ball(GameSprite):
    pass




platform = Platform(img_platform, 50, 300, 2)
platform2 = Platform(img_platform, 300, 200, 3)


game = True

finish = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False



    if finish == 0:        
        window.blit(img_back, (0, 0))
        platform.draw()
        platform.control()




    display.update()