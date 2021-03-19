import pygame
import numpy as np
import functions as fn
import random
import sys, os

np.set_printoptions(threshold=sys.maxsize)

blue_map_a, Gamemap_x, Gamemap_y = fn.Createmap()

game_order = [i for i in range(1,17)]; random.shuffle(game_order)
#파이게임 시작
pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

screen_width = 640
screen_height = 900
darkorchid = (153, 50, 204)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (8, 164, 236)
red = (144, 4, 20)
purple = (168, 76, 164)
brown = (192, 124, 84)
space_size = 40
GRIDLINECOLOR = (30, 30, 30)

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Ricochet game")

background = pygame.image.load(fn.resource_path("Ricochet_background.png"))

character_map = fn.Create_character_map()

character_red, character_red_x_pos, character_red_y_pos = fn.Create_character(fn.resource_path("character_red.png"), character_map)
character_blue, character_blue_x_pos, character_blue_y_pos = fn.Create_character(fn.resource_path("character_blue.png"), character_map)
character_brown, character_brown_x_pos, character_brown_y_pos = fn.Create_character(fn.resource_path("character_brown.png"), character_map)
character_purple, character_purple_x_pos, character_purple_y_pos = fn.Create_character(fn.resource_path("character_purple.png"), character_map)
character_black, character_black_x_pos, character_black_y_pos = fn.Create_character(fn.resource_path("character_black.png"), character_map)

font = pygame.font.Font('Roboto-Black.ttf', 32)
text = font.render('number of moved', True, black)
textRect = text.get_rect()
textRect.center = (320, 700)

moved_number = 0 
game_number = 0
current_select = 0
mouse_x_tran = 0
mouse_y_tran = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_x_tran = mouse_x//40 + 1
            mouse_y_tran = mouse_y//40 + 1
            current_select = character_map[mouse_y_tran-1][mouse_x_tran-1]

        if event.type == pygame.KEYDOWN:
            moved_number += 1
            if current_select == 1 or current_select == 2 or current_select == 3 or current_select == 4 or current_select == 5:
                [mouse_y_tran, mouse_x_tran] = np.where(character_map == current_select)
                mouse_y_tran = mouse_y_tran[0]+1
                mouse_x_tran = mouse_x_tran[0]+1
                if event.key == pygame.K_LEFT:
                    for ii in range(0,16):
                        if (mouse_x_tran-2-ii) == -1 or character_map[mouse_y_tran-1][mouse_x_tran-2-ii] > 0:
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran-1][mouse_x_tran-1-ii] = current_select
                            if current_select < 2:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] == 0:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] < 5:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 3:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] < 13:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] < 17:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 4:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] < 5:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] < 9:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 5:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] < 9:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] < 13:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            break
                        elif Gamemap_y[mouse_y_tran-1][mouse_x_tran-1-ii] == 4 :
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran-1][mouse_x_tran-1-ii] = current_select
                            if current_select < 2:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] == 0:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] < 5:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 3:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] < 13:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] < 17:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 4:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] < 5:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] < 9:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 5:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] < 9:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] < 13:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1-ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            break
                    if ii==0:
                        moved_number -= 1
                            
                if event.key == pygame.K_RIGHT:
                    if mouse_x_tran == 16:
                        moved_number -= 1
                        break
                    for ii in range(0,16):
                        if (mouse_x_tran-1+ii) == 15 or character_map[mouse_y_tran-1][mouse_x_tran+ii] > 0 :
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran-1][mouse_x_tran-1+ii] = current_select
                            if current_select < 2:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] == 0:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] < 5:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 3:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] < 13:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] < 17:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 4:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] < 5:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] < 9:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 5:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] < 9:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] < 13:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            break
                        if Gamemap_y[mouse_y_tran-1][mouse_x_tran+ii] == 4:
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran-1][mouse_x_tran+ii-1] = current_select
                            if current_select < 2:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] == 0:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] < 5:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 3:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] < 13:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] < 17:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 4:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] < 5:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] < 9:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 5:
                                if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] < 9:
                                    break
                                elif blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] < 13:
                                    if blue_map_a[mouse_y_tran-1][mouse_x_tran-1+ii] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            break
                    if ii==0:
                        moved_number -= 1
                    
                if event.key == pygame.K_UP:
                    for ii in range(0,16):
                        if (mouse_y_tran-ii-2) == -1 or character_map[mouse_y_tran-ii-2][mouse_x_tran-1] > 0:
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran-ii-1][mouse_x_tran-1] = current_select
                            if current_select < 2:
                                if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] == 0:
                                    break
                                elif blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] < 5:
                                    if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 3:
                                if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] < 13:
                                    break
                                elif blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] < 17:
                                    if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 4:
                                if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] < 5:
                                    break
                                elif blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] < 9:
                                    if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 5:
                                if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] < 9:
                                    break
                                elif blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] < 13:
                                    if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            break
                        elif Gamemap_x[mouse_y_tran-ii-1][mouse_x_tran-1] == 5:
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran-ii-1][mouse_x_tran-1] = current_select
                            if current_select < 2:
                                if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] == 0:
                                    break
                                elif blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] < 5:
                                    if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 3:
                                if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] < 13:
                                    break
                                elif blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] < 17:
                                    if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 4:
                                if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] < 5:
                                    break
                                elif blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] < 9:
                                    if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 5:
                                if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] < 9:
                                    break
                                elif blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] < 13:
                                    if blue_map_a[mouse_y_tran-ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            break
                    if ii==0:
                        moved_number -= 1
                    
                if event.key == pygame.K_DOWN:
                    if mouse_y_tran == 16:
                        moved_number -= 1
                        break
                    for ii in range(0,16):
                        if  (mouse_y_tran+ii-1) == 15 or character_map[mouse_y_tran+ii][mouse_x_tran-1] > 0 :
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran+ii-1][mouse_x_tran-1] = current_select
                            if current_select < 2:
                                if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] == 0:
                                    break
                                elif blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] < 5:
                                    if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 3:
                                if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] < 13:
                                    break
                                elif blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] < 17:
                                    if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 4:
                                if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] < 5:
                                    break
                                elif blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] < 9:
                                    if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 5:
                                if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] < 9:
                                    break
                                elif blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] < 13:
                                    if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            break
                        elif Gamemap_x[mouse_y_tran+ii][mouse_x_tran-1] == 5:
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran+ii-1][mouse_x_tran-1] = current_select
                            if current_select < 2:
                                if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] == 0:
                                    break
                                elif blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] < 5:
                                    if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 3:
                                if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] < 13:
                                    break
                                elif blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] < 17:
                                    if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 4:
                                if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] < 5:
                                    break
                                elif blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] < 9:
                                    if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            elif current_select < 5:
                                if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] < 9:
                                    break
                                elif blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] < 13:
                                    if blue_map_a[mouse_y_tran+ii-1][mouse_x_tran-1] == game_order[game_number] :
                                        game_number = game_number+1
                                        moved_number = 0
                                        break
                            break
                    if ii==0:
                        moved_number -= 1
        
    answer_color, answer_screen_x_pos, answer_screen_y_pos = fn.Answer_location(game_order, game_number, blue_map_a)
             
    red_y_pos, red_x_pos = np.where(character_map == 1) 
    character_red_x_pos = space_size * red_x_pos + 5
    character_red_y_pos = space_size * red_y_pos + 5

    blue_y_pos, blue_x_pos = np.where(character_map == 2)
    character_blue_x_pos = space_size * blue_x_pos + 5
    character_blue_y_pos = space_size * blue_y_pos + 5

    brown_y_pos, brown_x_pos = np.where(character_map == 3)
    character_brown_x_pos = space_size * brown_x_pos + 5
    character_brown_y_pos = space_size * brown_y_pos + 5

    purple_y_pos, purple_x_pos = np.where(character_map == 4)
    character_purple_x_pos = space_size * purple_x_pos + 5
    character_purple_y_pos = space_size * purple_y_pos + 5

    black_y_pos, black_x_pos = np.where(character_map == 5)
    character_black_x_pos = space_size * black_x_pos + 5
    character_black_y_pos = space_size * black_y_pos + 5

    moved_number_text = font.render(str(moved_number), True, black)
    movedRect =moved_number_text.get_rect()
    movedRect.center = (320, 750)
    
    screen.fill(white)
    screen.blit(answer_color, (answer_screen_x_pos, answer_screen_y_pos))
    screen.blit(character_black, (character_black_x_pos, character_black_y_pos))
    screen.blit(character_blue, (character_blue_x_pos, character_blue_y_pos))
    screen.blit(character_brown, (character_brown_x_pos, character_brown_y_pos))
    screen.blit(character_purple, (character_purple_x_pos, character_purple_y_pos))
    screen.blit(character_red, (character_red_x_pos, character_red_y_pos))
    

    for x in range(0, 16):
        # Draw the horizontal lines.
        startx = (x * space_size)
        starty = 0
        endx = (x * space_size)
        endy = (screen_width)
        pygame.draw.line(screen, GRIDLINECOLOR, (startx, starty), (endx, endy))
    for y in range(0, 16):
        # Draw the vertical lines.
        startx = 0
        starty = (y * space_size)
        endx = (screen_width * space_size)
        endy = (y * space_size)
        pygame.draw.line(screen, GRIDLINECOLOR, (startx, starty), (endx, endy))
    for ii in range(0, 17):
        for jj in range(0, 16):
            if Gamemap_x[ii][jj] == 5:
                startx = space_size * jj
                starty = space_size * ii
                endx = space_size * (jj+1)
                endy = starty
                pygame.draw.line(screen, GRIDLINECOLOR, (startx, starty), (endx, endy), width=5)
    for ii in range(0, 16):
        for jj in range(0, 17):
            if Gamemap_y[ii][jj] == 4:
                startx = space_size * jj
                starty = space_size * ii
                endx = space_size * jj
                endy = space_size * (ii+1)
                pygame.draw.line(screen, GRIDLINECOLOR, (startx, starty), (endx, endy), width=5)
    
    pygame.draw.line(screen, GRIDLINECOLOR, (280, 280), (280, 360), width=5)
    pygame.draw.line(screen, GRIDLINECOLOR, (280, 280), (360, 280), width=5)
    pygame.draw.line(screen, GRIDLINECOLOR, (360, 280), (360, 360), width=5)
    pygame.draw.line(screen, GRIDLINECOLOR, (280, 360), (360, 360), width=5)
    screen.blit(text,textRect)  
    screen.blit(moved_number_text,movedRect)

    pygame.display.update()
    fpsClock.tick(FPS)


pygame.quit()
