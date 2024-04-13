import pygame


pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 900, 550
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
LIGHT_GREY = (192, 192, 192)
mw = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PingPong')

class Object:

    points = 0

    def __init__(self, GameSprite_image, GameSprite_x, GameSprite_y, GameSprite_size):
        self.image = pygame.transform.scale(pygame.image.load(GameSprite_image).convert_alpha(), GameSprite_size)
        self.rect = self.image.get_rect()
        self.rect.x = GameSprite_x
        self.rect.y = GameSpritet_y

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


def render_score(racket): 
    result = ''
    if racket.points < 10:
        result = '0' + str(racket.points)
    else:
        result = str(racket.points)

racket_one = GameSprite('1.png', 20, 185, (20, 150))
racket_two = GameSprite('2.png', 860, 185, (20, 150))

ball = GameSprite('3.png', 435, 255, (40, 40))
ball_speed_x = 4
ball_speed_y = 4

win = pygame.transform.scale(pygame.image.load("win.png"), (200, 100))
lose = pygame.transform.scale(pygame.image.load("lose.png"), (200, 100))
restart = pygame.transform.scale(pygame.image.load("restart.jpg"), (200, 100))


clock = pygame.time.Clock()
FPS = 60
game = True
finish = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if not finish:
        mw.fill((200, 200, 200))       

        ball.draw()
        racket_one.draw()
        racket_two.draw()
        border_one = pygame.draw.rect(mw, WHITE, pygame.Rect(0, 0, 900, 15))
        border_two = pygame.draw.rect(mw, WHITE, pygame.Rect(0, 535, 900, 15))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and racket_one.rect.y > 20:
            racket_one.rect.y -= 5
        if keys[pygame.K_s] and racket_one.rect.y < 375:
            racket_one.rect.y += 5
        if keys[pygame.K_UP] and racket_two.rect.y > 20:
            racket_two.rect.y -= 5
        if keys[pygame.K_DOWN] and racket_two.rect.y < 375:
            racket_two.rect.y += 5

        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        if ball.rect.colliderect(border_one):
            ball_speed_y *= -1
        if ball.rect.colliderect(border_two):
            ball_speed_y *= -1
        if ball.rect.colliderect(racket_one.rect):
            ball_speed_x *= -1
        if ball.rect.colliderect(racket_two.rect):
            ball_speed_x *= -1

        if ball.rect.x >= 860:
            racket_one.points += 1
            ball.rect.x = 435
            ball.rect.y = 255

        if ball.rect.x <= -5:
            racket_two.points += 1
            ball.rect.x = 435
            ball.rect.y = 255

        if racket_one.points >= 10:
            mw.blit(win, (110, 190))
            mw.blit(lose, (600, 190))
            finish = True
       


        if racket_two.points >= 10:
            mw.blit(win, (600, 190))
            mw.blit(lose, (110, 190))
            finish = True

            
    else:
        rect_button = pygame.draw.rect(mw, WHITE, pygame.Rect(350, 400, 200, 100))
        main_button = pygame.draw.rect(mw, BLACK, pygame.Rect(357, 407, 186, 86))
        mw.blit(restart, (350, 400))

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if main_button.collidepoint(x, y):
                finish = False
                racket_one.points = 0
                racket_two.points = 0
                racket_one.rect.x = 20
                racket_one.rect.y = 185
                racket_two.rect.x = 860
                racket_two.rect.y = 185

    clock.tick(FPS)
    pygame.display.update()
