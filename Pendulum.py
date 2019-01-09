import pygame

pygame.init()

display_width = 1000
display_height = 750

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)
GREEN = (0,255,0)
RED =   (255,0,0)

DISPLAYSURF = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pendulums')

done = False
clock = pygame.time.Clock()

while not done:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    DISPLAYSURF.fill(WHITE)
    
    pygame.draw.circle(DISPLAYSURF, BLUE, (int(display_width/2),int(display_height/2)), 40)
    
    pygame.display.flip()
 
pygame.quit()