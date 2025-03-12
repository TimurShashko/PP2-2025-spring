import pygame

pygame.init() # initializes all the pygame sub-modules

WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # creating a game window
# set_mode() takes a tuple as an argument

COLOR_RED = (255, 0, 0) 

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

movement_speed = 20

running = True

# this object allows us to set the FPS
clock = pygame.time.Clock()
FPS = 60 

while running: # game loop
    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()       
    if pressed_keys[pygame.K_UP]:
        circle_y -= movement_speed
    if pressed_keys[pygame.K_DOWN]:
        circle_y += movement_speed
    if pressed_keys[pygame.K_RIGHT]:
        circle_x += movement_speed
    if pressed_keys[pygame.K_LEFT]:
        circle_x -= movement_speed

    if circle_x - 25 < 0:
        circle_x = 25
    if circle_x + 25 > WIDTH:
        circle_x = WIDTH - 25
    if circle_y - 25 < 0:
        circle_y = 25
    if circle_y + 25 > HEIGHT:
        circle_y = HEIGHT - 25

    screen.fill("white")
    pygame.draw.circle(screen, COLOR_RED, (circle_x, circle_y), 25)

    
    pygame.display.flip() # updates the screen
    clock.tick(FPS) # sets the FPS
    # delay is 1000.0 / FPS