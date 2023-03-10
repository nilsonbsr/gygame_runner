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
# convert_alpha method make our imported graphic easier for python to use
sky_surf = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
#snail_x_pos = 600
# render(text, AA, color) AA means anti-aliasing which basically means we are going to smooth the edges of the text
score_surf = test_font.render('My game', False, 'Black')
# we position our text in the center of the screen
score_rect = score_surf.get_rect(center = (400, 50))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
# to place a player on the surface we need to create a rectangle and this should have the exact size as player_surface
player_rect = player_surf.get_rect(midbottom = (80, 300))
# 300 is height value of our ground
snail_rect = snail_surf.get_rect(bottomright = (600, 300))


while True:
    # event loop which is technically responsible for all the player input and see if one of them happening
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # this while True loop will be False and
            # we don't get error in our console
            exit()
        # this would give us a mouse position and will only triggerd if we moved the mouse
        #if event.type == pygame.MOUSEMOTION:
         #   if player_rect.collidepoint(event.pos):
          #      print('Collision')


    # draw all our elements

    # attach test_surface to display surface
    # blit stands for block instance transfer it takes 2 arguments the surface we want to place and the position
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))
    # with the draw module we draw a certain thing in our case rectangle
    # we need to specify where we want to draw, color and finally the actual rectangle we want to draw
    pygame.draw.rect(screen, 'Pink',  score_rect)
    pygame.draw.rect(screen, 'Pink',  score_rect, 10)
    
    screen.blit(score_surf, score_rect)
    # making animation by changing the position of our variable
    # snail_x_pos -= 4

    # once the snail leaving the screen it keeps on moving to the left. In order to prevent this we need to set our position
    # to a higher value
    # if (snail_x_pos < -100):
    #    snail_x_pos = 800

    # moving snail
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        # 800 is the right side of our screen
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    # moving out player using rectangle for its position (we actually don't move player but the rectangle we draw around out player
    player_rect.left += 1
    # we are taking the player surface and replace it of position of the rectangle
    screen.blit(player_surf, player_rect)

    # collision
   # mouse_pos = pygame.mouse.get_pos()
   # if player_rect.collidepoint(mouse_pos):
    #    print(pygame.mouse.get_pressed())




    # update everything
    pygame.display.update()
    # this 60 tells that this while True loop should not run faster than 60 fps (basically frame rate)
    clock.tick(60)
