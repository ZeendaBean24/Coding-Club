import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My Game')
player_image = pygame.image.load("image.png")
player_image = pygame.transform.scale(player_image, (50, 50))
playerSpeed = 7
player_x, player_y = 100, 600

gravity = 0.5
jump_speed = 15
player_y_velocity = 0
is_jumping = False
GROUND_HEIGHT = 600
run = True
while run:
    screen.fill((0, 0, 0))
    key = pygame.key.get_pressed()
    pygame.draw.rect(screen, (34, 139, 34), (0, GROUND_HEIGHT+50, SCREEN_WIDTH, GROUND_HEIGHT+50))
    if key[pygame.K_a]:
        player_x -= playerSpeed
    if key[pygame.K_d]:
        player_x += playerSpeed    
    # if key[pygame.K_w]:
    #     player_y -= playerSpeed
    # if key[pygame.K_s]:
    #     player_y += playerSpeed

    if key[pygame.K_w] and not is_jumping:
        is_jumping = True
        player_y_velocity = -jump_speed
    if is_jumping:
        player_y += player_y_velocity
        player_y_velocity += gravity
    
    if player_y >= 600:  
        player_y = 600
        is_jumping = False
        player_y_velocity = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if player_y >= SCREEN_HEIGHT-50:  
        player_y = SCREEN_HEIGHT-50
        is_jumping = False
        player_y_velocity = 0
    
    if player_x < 0:  
        player_x = 0
    elif player_x > SCREEN_WIDTH-50: 
        player_x = SCREEN_WIDTH-50
    screen.blit(player_image, (player_x, player_y))
    pygame.display.update()

pygame.quit()