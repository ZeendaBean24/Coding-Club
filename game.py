import pygame

# Initialize Pygame
pygame.init()

# Set the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My Game')

# Load and transform the player image
player_image = pygame.image.load("image.png")
player_image = pygame.transform.scale(player_image, (50, 50))

# Player attributes
playerSpeed = 7
player_x, player_y = 100, 600

# Platform attributes
platform_x, platform_y, platform_width, platform_height = 300, 500, 200, 20

# Obstacle attributes
obstacle_x, obstacle_y, obstacle_width, obstacle_height = 400, 480, 50, 20

# Goal attributes
goal_x, goal_y, goal_width, goal_height = 700, 550, 50, 50

# Physics attributes
gravity = 0.5
jump_speed = 15
player_y_velocity = 0
is_jumping = False

# Ground level
GROUND_HEIGHT = 600

# Game loop flag
run = True

while run:
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Process input
    key = pygame.key.get_pressed()

    # Draw ground
    pygame.draw.rect(screen, (34, 139, 34), (0, GROUND_HEIGHT+50, SCREEN_WIDTH, GROUND_HEIGHT+50))

    # Draw the platform
    pygame.draw.rect(screen, (105, 105, 105), (platform_x, platform_y, platform_width, platform_height))

    # Collision detection with the platform
    if player_x + 50 > platform_x and player_x < platform_x + platform_width and player_y + 50 >= platform_y and player_y < platform_y + platform_height:
        player_y = platform_y - 50
        is_jumping = False
        player_y_velocity = 0

    # Move the player
    if key[pygame.K_a]:
        player_x -= playerSpeed
    if key[pygame.K_d]:
        player_x += playerSpeed    

    # Player jump logic
    if key[pygame.K_w] and not is_jumping:
        is_jumping = True
        player_y_velocity = -jump_speed

    # Apply gravity
    if is_jumping:
        player_y += player_y_velocity
        player_y_velocity += gravity

    # Stop the player at the ground level
    if player_y >= GROUND_HEIGHT - 50:  
        player_y = GROUND_HEIGHT - 50
        is_jumping = False
        player_y_velocity = 0

    # Check for game quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Keep the player within the screen bounds
    if player_x < 0:  
        player_x = 0
    elif player_x > SCREEN_WIDTH - 50:
        player_x = SCREEN_WIDTH - 50

    # Draw the player
    screen.blit(player_image, (player_x, player_y))

    # Draw the obstacle and goal within the game loop to ensure they are updated on the screen
    pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    pygame.draw.rect(screen, (0, 0, 255), (goal_x, goal_y, goal_width, goal_height))

    # Game logic for obstacle collision and reaching the goal
    # Check if player collides with the obstacle
    if player_x < obstacle_x + obstacle_width and player_x + 50 > obstacle_x and player_y + 50 > obstacle_y and player_y < obstacle_y + obstacle_height:
        print("Game Over!")  # Placeholder for game over logic
        run = False

    # Check if player reaches the goal
    if player_x < goal_x + goal_width and player_x + 50 > goal_x and player_y + 50 > goal_y and player_y < goal_y + goal_height:
        print("Level Complete!")  # Placeholder for level completion logic
        run = False

    # Update the display
    pygame.display.update()

pygame.quit()