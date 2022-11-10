#Download Pygame from Windows Command
import pygame
#Exit Funcition
from sys import exit

pygame.init() #settings Pygame
#set up Screen
screen = pygame.display.set_mode((800, 400))
#Title
pygame.display.set_caption('Cyber')
#Clock
clock = pygame.time.Clock()
#font
font = pygame.font.Font('d:/Software engineering/project2/fonts/ChunkFive-Regular.otf', 30)

#variable
sky_surface = pygame.image.load('d:/Software engineering/project2/Graphics/skyl.png').convert() # it will be faster for png files
ground_surface = pygame.image.load('d:/Software engineering/project2/Graphics/ground1.png').convert()
text_surface = font.render('MacroTech Game !', False, '#824696').convert()
snail_surface = pygame.image.load('d:/Software engineering/project2/Graphics/snail/snail1.png').convert_alpha()
snail_x_position = 600
#Loop
while True:
    for event in pygame.event.get(): #all events
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
             
    screen.blit(sky_surface,(0, 0))
    screen.blit(ground_surface,(0, 300))
    screen.blit(text_surface,(250, 50))
    snail_x_position -= 0.099
    if snail_x_position < -100: snail_x_position = 800
    screen.blit(snail_surface, (snail_x_position,250))
    
    
    #draw all our elements
    #update everything
    pygame.display.update()
    