import pygame

pygame.init()

# Set up window
WIDTH, HEIGHT= 800, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Holly Jolly Snowball Fight!")
run = True

# Colors
WHITE = (255, 255, 255)

# Ball Varibales
radius = 10
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 1, 1

# Paddle Dimensions
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH -(100 - paddle_width/2)



# Main Loop
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    # Movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    # Objects
    pygame.draw.circle(wn, WHITE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, WHITE, pygame.Rect(left_paddle_x, 
    left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, WHITE, pygame.Rect(right_paddle_x, 
    right_paddle_y, paddle_width, paddle_height))

    pygame.display.update()