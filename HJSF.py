import pygame
import os
import sys

pygame.init()

"""
    To TURN IN : We have to record this and upload to youtube !!
    Screen record, put into box, voice record w/ vid playing and talk over.
    Upload to YT but keep it as unlisted, and SET THE LINK in the "read me:" part of your code!
    
"""
#Common : Screen Setting
WIDTH, HEIGHT = 700, 500
WN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Holly Jolly Snowball Fight!")

FPS = 60

#Common : Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

##Common : Game Setting
BALL_RADIUS = 7
PLAYER_WIDTH, PLAYER_HEIGHT = 130, 159
SCORE_FONT = pygame.font.SysFont("comicsans", 50)
WINNING_SCORE = 10

# Adding backgrounds
BG_IMAGE = pygame.image.load('snowy_bg.png')

#Common Player Class:
class Players:
    VEL = 4

    def __init__(self, x, y, idle_image_path, hit_image_path):
        self.image_idle = pygame.image.load(idle_image_path).convert_alpha()
        self.image_hit = pygame.image.load(hit_image_path).convert_alpha()
        self.image = self.image_idle
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hit_timer = 0

    
    def draw(self, win):
        win.blit(self.image, self.rect)

    def update(self):
        #if hit. timer will activate, and reset!
        if self.hit_timer > 0:
            self.hit_timer -= 1
        # Then revert to neutral image.
        else:
            self.image = self.image_idle
    #Detect hit or not

    def on_hit(self):
        self.image = self.image_hit
        self.hit_timer = 10 # Hit image appear time.
    
    def move(self, up=True):
        if up:
            self.rect.y -= self.VEL
        else:
            self.rect.y += self.VEL

    def reset(self, x,y):
        self.rect.x = x
        self.rect.y = y


class Ball:
    MAX_VEL = 5

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1

# Draws game elements on screen:
def draw(WN, player_1, player_2, ball, left_score, right_score):
    WN.blit(BG_IMAGE, (0,0))

    #Draws Score
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    WN.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    WN.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width()//2, 20))
    
    #Creates Dashed Border
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(WN, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))
    
    #Draw Players and Ball!
    player_1.draw(WN)
    player_2.draw(WN)
    ball.draw(WN)

    pygame.display.update()



def handle_collision(ball, player_1, player_2):

    #Adds bounce :
    if ball.y + ball.radius >= HEIGHT or  ball.y - ball.radius <= 0:
        ball.y_vel *= -1
    
    # Collision w/Player 1:
    """collide rect in pygame checks is there are 2 or more
    rectangles/sprites are colliding.
    
    first we get the dimension in the ball """
    if player_1.rect.colliderect(pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)):
        ball.x_vel *= -1
        player_1.on_hit()
    
     # Collision w/Player 2:
    if player_2.rect.colliderect(pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)):
        ball.x_vel *= -1
        player_2.on_hit()

"""
    Here we're swapping the self.x with self.rect.y, we're looking for the rect!
    """
def player_paddle_movement(keys, player_1, player_2):

    #player 1
    if keys[pygame.K_w] and player_1.rect.y - player_1.VEL >= 0:
        player_1.move(up=True)
    if keys[pygame.K_s] and player_1.rect.y + player_1.VEL + player_1.rect.height <= HEIGHT:
        player_1.move(up=False)

    #player 2
    if keys[pygame.K_UP] and player_2.rect.y - player_2.VEL >= 0:
        player_2.move(up=True)
    if keys[pygame.K_DOWN] and player_2.rect.y + player_2.VEL + player_2.rect.height <= HEIGHT:
        player_2.move(up=False)

# Here, we need to adjust the original code's padding off the walls so our character acturally fits!!!
def main():
    clock = pygame.time.Clock()

    player_1 = Players(0, HEIGHT //2 - PLAYER_HEIGHT //2, 'rud_neutral.png', 'rud_hit.png')
    player_2 = Players(WIDTH - PLAYER_WIDTH + 2, HEIGHT //2 - PLAYER_HEIGHT //2, 'comet_neutral.png', 'comet_hit.png')
    ball = Ball(WIDTH //2, HEIGHT //2, BALL_RADIUS)

    #Start scores
    left_score = 0
    right_score = 0

    # We have to draw all things/ game elements first before run=True.
    run = True

    while run:
        clock.tick(FPS)

        #draw(WN, ball, left_score, right_score)

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # break

        # Player Movement
        keys = pygame.key.get_pressed()
        player_paddle_movement(keys, player_1, player_2)

        #Ball Movement
        ball.move()
        handle_collision(ball, player_1, player_2)

        player_1.update()
        player_2.update()

        WN.blit(BG_IMAGE, (0, 0))
        player_1.draw(WN)
        player_2.draw(WN)
        ball.draw(WN)

        # Score Logic
        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        # Win Condition
        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "❄️ Rudolph Wins! ❄️"
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "❄️ Comet Wins! ❄️"

        if won:
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WN.blit(text, (WIDTH//2 - text.get_width() // 2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            player_1.reset(WIDTH // 20, HEIGHT //2 - PLAYER_HEIGHT //2)
            player_2.reset(WIDTH - PLAYER_WIDTH - WIDTH // 20, HEIGHT // 2 - PLAYER_HEIGHT // 2)
            left_score = 0
            right_score = 0

        draw(WN, player_1, player_2, ball, left_score, right_score)

    pygame.quit()


if __name__ == '__main__':
    main()