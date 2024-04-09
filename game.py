import pygame
 
# Initialize Pygame
pygame.init()
 
# Set the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My Game')
 
# Load and transform the player image
# Ensure you have an 'image.png' in your project directory or adjust this line accordingly
player_image = pygame.image.load("image.png")
player_image = pygame.transform.scale(player_image, (50, 50))
 
# Player attributes
player_speed = 7
player_x, player_y = 50, SCREEN_HEIGHT-70
player_width, player_height = 50, 50
 
# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (185, 185, 185)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# Create a pygame.Rect object for the player for easier collision handling
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
 
# Platform attributes - List of platforms (x, y, width, height)
platforms = [(0, SCREEN_HEIGHT-20, SCREEN_WIDTH, 20),
             (150, SCREEN_HEIGHT-100, 100, 20),
             (350, SCREEN_HEIGHT-180, 200, 20),
             (550, SCREEN_HEIGHT-260, 100, 20)]
 
end = (650, SCREEN_HEIGHT-460, 60, 60)
 
# Physics attributes
gravity = 0.7
jump_strength = 15
player_y_velocity = 0
is_jumping = False
 
# Game loop flag
run = True
 
while run:
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    player_x += (keys[pygame.K_d] - keys[pygame.K_a]) * player_speed
 
    # Jumping
    if keys[pygame.K_w] and not is_jumping:
        player_y_velocity = -jump_strength
        is_jumping = True  # Player leaves the ground
 
    # Update player position with gravity
    player_y += player_y_velocity
    player_y_velocity += gravity
 
    # Check for collision with platforms
    player_rect.update(player_x, player_y, player_width, player_height)
    is_jumping = True 
    for plat in platforms:
        plat_rect = pygame.Rect(plat[0], plat[1], plat[2], plat[3])
        if player_rect.colliderect(plat_rect):
            if player_y_velocity > 0:
                player_y = plat_rect.top - player_height
                player_y_velocity = 0
                is_jumping = False
            elif player_y_velocity < 0:
                player_y = plat_rect.bottom
                player_y_velocity = 0
                hit_ceiling = True
 
    # Prevent the player from going out of bounds
    player_x = max(0, min(SCREEN_WIDTH - player_width, player_x))
    player_y = max(0, min(SCREEN_HEIGHT - player_height, player_y))
 
    # Draw platforms
    for plat in platforms:
        pygame.draw.rect(screen, GRAY, plat)
 
    pygame.draw.rect(screen, RED, end)
    end_rect = pygame.Rect(end[0], end[1], end[2], end[3])
    if player_rect.colliderect(end_rect):
        # placeholder
        print("Level Complete!")
        run = False
 
    # Draw the player
    screen.blit(player_image, (player_x, player_y))
    pygame.display.update()
 
pygame.quit()