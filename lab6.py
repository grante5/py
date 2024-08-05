import pygame
import sys


pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Display Red Triangle")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


running = True
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
               
                pygame.draw.polygon(screen, RED, [
                    (width // 2, height // 2 - 50),
                    (width // 2 - 50, height // 2 + 50),
                    (width // 2 + 50, height // 2 + 50)
                ])
            elif event.button == 3:  
                running = False

   
    pygame.display.flip()


pygame.quit()
sys.exit()
