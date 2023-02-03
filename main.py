import pygame
from sys import exit

pygame.init()
# display surface is the window the players is going to see
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
# clock object helps us with time and frame rate
clock = pygame.time.Clock()
# display surface and regular surface (screen) has lots of in common and we display it in while True
test_surface = pygame.Surface((100, 200))
test_surface.fill('Red ')


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
    screen.blit(test_surface, (200,100))
    # this 60 tells that this while True loop should not run faster than 60 fps
    clock.tick(60)
