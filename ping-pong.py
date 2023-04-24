from pygame import*
window = display.set_mode((1000,700))
display.set_caption('ОКОШКО')
fon = transform.scale(image.load('aфон.png'),(1000,700))
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self,picture,x,y,w,h,speed):
        super().__init__()
        self.picture = transform.scale(image.load(picture),(w,h))
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.picture,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y> 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 610:
            self.rect.y += self.speed
    def move2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y> 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 610:
            self.rect.y += self.speed
platform1 = Player('платформа 1.png',20,300,30,90,10)
platform2 = Player('платформа 2.png',930,300,30,90,10)
ball = GameSprite('мячь.png', 470,330,50,50,5)
s_x = 5
s_y = 5
game = True
while game:
    clock.tick(60)
    window.blit(fon,(0,0))
    platform1.move2()
    platform1.reset()
    platform2.move()
    platform2.reset()
    ball.rect.x += s_x
    ball.rect.y += s_y
    if ball.rect.y >= 650:
        s_y *= -1
    if ball.rect.y <= 0:
        s_y *= -1
    if sprite.collide_rect(ball,platform1):
        s_x *= -1
    if sprite.collide_rect(ball,platform2):
        s_x *= -1
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
