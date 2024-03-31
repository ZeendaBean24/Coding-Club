import pygame

pygame.init() # Game Window

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

player = pygame.Rect((300, 250, 50, 50))

run = True
while run:
	
	for event in pygame.event.get(): # Loops through all the events that Pygame picks up
		if event.type == pygame.QUIT: # Check if the user is clicking the X button
			run = False

pygame.quit()

