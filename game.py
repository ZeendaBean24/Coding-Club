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

# Define platform dimensions and position
platform_x, platform_y, platform_width, platform_height = 300, 500, 200, 20

# Define obstacle dimensions and position
obstacle_x, obstacle_y, obstacle_width, obstacle_height = 400, 480, 50, 20

# Draw the obstacle
pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

# Define the goal dimensions and position
goal_x, goal_y, goal_width, goal_height = 700, 550, 50, 50

# Draw the goal
pygame.draw.rect(screen, (0, 0, 255), (goal_x, goal_y, goal_width, goal_height))

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

    # Draw platform
    pygame.draw.rect(screen, (105, 105, 105), (platform_x, platform_y, platform_width, platform_height))

    # Check for collisions with the platform to allow the player to land
    if player_x < platform_x + platform_width and player_x + 50 > platform_x and player_y + 50 > platform_y and player_y < platform_y + platform_height:
        player_y = platform_y - 50
        is_jumping = False
        player_y_velocity = 0

    # Game logic for obstacle collision and reaching the goal
    # Check if player collides with the obstacle
    if player_x < obstacle_x + obstacle_width and player_x + 50 > obstacle_x and player_y + 50 > obstacle_y and player_y < obstacle_y + obstacle_height:
        print("Game Over!")  # Placeholder for game over logic
        run = False

    # Check if player reaches the goal
    if player_x < goal_x + goal_width and player_x + 50 > goal_x and player_y + 50 > goal_y and player_y < goal_y + goal_height:
        print("Level Complete!")  # Placeholder for level completion logic
        run = False

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