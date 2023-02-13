import pygame
from sys import exit

pygame.init()
# display surface is the window the players is going to see
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
# clock object helps us with time and frame rate
clock = pygame.time.Clock()
# create font
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)



# display surface and regular surface (screen) has lots of in common and we display it in while True
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 600
# render(text, AA, color) AA means anti-aliasing which basically means we are going to smooth the edges of the text
text_surface = test_font.render('My game', False, 'Black')


while True:
    # event loop which is technically responsible for all the player input and see if one of them happening
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # this while True loop will be False and
            # we don't get error in our console
            exit()

    # draw all our elements
    # update everything
    pygame.display.update()
    # attach test_surface to display surface
    # blit stands for block instance transfer it takes 2 arguments the surface we want to place and the position
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300, 50))
    # making animation by changing the position of our variable
    snail_x_pos -= 4
    # once the snail leaving the screen it keeps on moving to the left. In order to prevent this we need to set our position
    # to a higher value
    if (snail_x_pos < -100):
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250))
    # this 60 tells that this while True loop should not run faster than 60 fps (basically frame rate) 
    clock.tick(60)
