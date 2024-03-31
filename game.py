import pygame

pygame.init() # Game Window

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

player = pygame.Rect((300, 250, 50, 50))

run = True
while run:

	screen.fill((0, 0, 0)) # Don't leave a trail

	pygame.draw.rect(screen, (255, 0, 0), player)

	# Player movement
	key = pygame.key.get_pressed()
	
	if key[pygame.K_a] == True:
		player.move_ip(-10, 0)
	elif key[pygame.K_d] == True:
		player.move_ip(10, 0)
	elif key[pygame.K_w] == True:
		player.move_ip(0, -10)
	elif key[pygame.K_s] == True:
		player.move_ip(0, 10)
	
	for event in pygame.event.get(): # Loops through all the events that Pygame picks up
		if event.type == pygame.QUIT: # Check if the user is clicking the X button
			run = False
			
	pygame.display.update() # Updates the rectangle

pygame.quit()