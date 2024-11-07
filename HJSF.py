import pygame

pygame.init()


# Set up window
WIDTH, HEIGHT = 800, 600
WN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Holly Jolly Snowball Fight!")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ALPHA = (255, 255, 255, 255)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100


class Paddle:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, WN):
        pygame.draw.rect(WN, self.COLOR, (self.x, self.y, self.width, self.height))
    
    def move (self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL


def draw(WN, paddles):
    WN.fill(BLACK)

    for paddle in paddles:
        paddle.draw(WN)
    
    pygame.display.update()
    
# Setting movemnet keys and borders for paddles.
def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)
    
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y - right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)



def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)


    while run:
        clock.tick(FPS)
        draw(WN, [left_paddle, right_paddle])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

    pygame.quit()


if __name__ == '__main__':
    main()