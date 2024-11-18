import pygame
import os
import sys
pygame.init()


WIDTH, HEIGHT = 700, 500
WN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Holly Jolly Snowball Fight!")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BALL_RADIUS = 7
PLAYER_1_WIDTH, PLAYER_1_WIDTH = 130, 159
PLAYER_2_WIDTH, PLAYER_2_WIDTH = 128, 153

SCORE_FONT = pygame.font.SysFont("comicsans", 50)
WINNING_SCORE = 10

# Adding backgrounds
BG_IMAGE = pygame.image.load('snowy_bg.png')



#rud neutral dimensions = 130 x 159
#rud hit dimensions = 147 x 159
class player_1:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y):
        img = pygame.image.load('rud_neutral.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


#comet neutral dimensions = 128 x 153
#comet hit dimensions = 143 x 153
class player_2:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y):
        img = pygame.image.load('')
    


    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


class Ball:
    MAX_VEL = 5
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1


def draw(WN, Rudolph, Comet, ball, left_score, right_score):
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    WN.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    WN.blit(right_score_text, (WIDTH * (3/4) -
                                right_score_text.get_width()//2, 20))
    
    #Below makes the line.
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(WN, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

    ball.draw(WN)
    pygame.display.update()


def handle_collision(ball, player_1, player_2):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= player_1.y and ball.y <= player_1.y + player_1.height:
            if ball.x - ball.radius <= player_1.x + player_1.width:
                ball.x_vel *= -1

                middle_y = player_1.y + player_1.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (player_1.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else:
        if ball.y >= player_2.y and ball.y <= player_2.y + player_2.height:
            if ball.x + ball.radius >= player_2.x:
                ball.x_vel *= -1

                middle_y = player_2.y + player_2.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (player_2.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


def player_paddle_movement(keys, player_1, player_2):
    if keys[pygame.K_w] and player_1.y - player_1.VEL >= 0:
        player_1.move(up=True)
    if keys[pygame.K_s] and player_1.y + player_1.VEL + player_1.height <= HEIGHT:
        player_1.move(up=False)

    if keys[pygame.K_UP] and player_2.y - player_2.VEL >= 0:
        player_2.move(up=True)
    if keys[pygame.K_DOWN] and player_2.y + player_2.VEL + player_2.height <= HEIGHT:
        player_2.move(up=False)

# Here, we need to adjust the original code's padding off the walls so our character acturally fits!!!
def main():
    run = True
    clock = pygame.time.Clock()

    player_1 = player_1(30, HEIGHT//2 - PLAYER_1_HEIGHT //
                         2, PADDLE_WIDTH, PLAYER_1_HEIGHT)
    player_2 = player_2(WIDTH - 30 - PADDLE_WIDTH, HEIGHT //
                          2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    left_score = 0
    right_score = 0

    while run:
        clock.tick(FPS)
        WN.blit(BG_IMAGE, (0, 0))
        draw(WN, [player_1, player_2], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        player_paddle_movement(keys, player_1, player_2)

        ball.move()
        handle_collision(ball, player_1, player_2)

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "❄️ Rudolph Wins! ❄️"
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "❄️ Comet Wins! ❄️"

        if won:
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WN.blit(text, (WIDTH//2 - text.get_width() //
                            2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            player_1.reset()
            player_2.reset()
            left_score = 0
            right_score = 0

    pygame.quit()


if __name__ == '__main__':
    main()