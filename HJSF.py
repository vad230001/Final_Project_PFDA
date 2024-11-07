import pygame

pygame.init()


# Set up window
WIDTH, HEIGHT = 700, 500
WN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Holly Jolly Snowball Fight!")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS =  8

"""
Also, we can use that one tile method used in our last lecture (notes in word) to add the a cute x-mas pattern.
Would it be okay to only have this as a duo match or should I implement a computor right paddle? The cp can be common deer, while player is rudolph!

"""
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


class Ball:
    MAX_VEL = 6
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, WN):
        pygame.draw.circle(WN, self.COLOR, (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel




# Making sure all are actually on scree, and making dashed line.
def draw(WN, paddles, ball):
    WN.fill(BLACK)

    for paddle in paddles:
        paddle.draw(WN)
  
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(WN, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))


    ball.draw(WN)
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
    


"""
Later! We have to implement reindeer characters here !! We must use both tutorials (and then some) to add these features!!
The reindeer will have to be swapped with the controllers.
"""
def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    # Getting the ball ROLLIN'.
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)


    while run:
        clock.tick(FPS)
        draw(WN, [left_paddle, right_paddle], ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()

    pygame.quit()


if __name__ == '__main__':
    main()