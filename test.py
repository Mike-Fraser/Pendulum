import pygame

pygame.init()

display_width = 1000
display_height = 750

red = (255,0,0)

DISPLAYSURF = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pendulums')



while True:

	for event in pygame.event.get():
		print(event)
	
	pygame.draw.circle(DISPLAYSURF, red, (display_width/2,display_width/2), 50, width=0)

	pygame.display.update()