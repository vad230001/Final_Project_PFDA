import pygame
pygame.init()


# Set up window
WIDTH, HEIGHT = 800, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Holly Jolly Snowball Fight!")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (255, 255, 255)
ALPHA = (255, 255, 255, 255)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100


class Paddle:
    COLOR = WHITE
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, wn):
        pygame.draw.rectangle(wn, self.COLOR, (self.x, self.y, self.width, self.height)))






def draw(wn):
    wn.fill(BLACK)
    pygame.display.update()
    

def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    while run:
        clock.tick(FPS)
        draw(wn)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


if __name__ == '__main__':
    main()