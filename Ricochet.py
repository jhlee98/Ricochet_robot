import pygame
import numpy as np
import functions as fn
import random
import sys

np.set_printoptions(threshold=sys.maxsize)

map1 = np.zeros((8,8)); map2 = np.zeros((8,8)); map3 = np.zeros((8,8)); map4 = np.zeros((8,8))
map1[0][2] = 3; map1[0][5] = 2; map1[1][5] = 1; map1[3][7] = 2; map1[4][3] = 2; map1[5][2] = 1
map1[7][1] = 1; map1[6][5] = 1; map1[6][6] = 2
map2[6][0] = 1; map2[5][1] = 2; map2[2][2] = 2; map2[3][2] = 1; map2[7][2] = 1; map2[1][3] = 1
map2[1][4] = 2; map2[5][6] = 3; map2[2][7] = 2
map3[4][0] = 1; map3[4][1] = 2; map3[7][1] = 1; map3[0][2] = 2; map3[1][2] = 1; map3[6][5] = 3
map3[1][5] = 1; map3[0][6] = 2; map3[2][7] = 2
map4[3][0] = 2; map4[4][0] = 1; map4[2][1] = 1; map4[1][1] = 2; map4[1][3] = 3; map4[6][3] = 1; map4[6][4] = 2
map4[7][2] = 1; map4[5][5] = 1; map4[4][6] = 2; map4[2][7] = 2
map1 = map1.T; map2 = map2.T; map3 = map3.T; map4 = map4.T
order = [1, 2, 3, 4] ; random.shuffle(order)
map5 = np.c_[fn.rotate_180(globals()['map{}'.format(order[0])]), np.rot90(globals()['map{}'.format(order[1])])]
map6 = np.c_[fn.rotate_270(globals()['map{}'.format(order[2])]), globals()['map{}'.format(order[3])]]
blue_map = np.concatenate((map5, map6), axis = 0)
Gamemap = np.zeros((33,33), dtype=int)
for ii in range(0,33):
    for jj in range(0,33):
        Gamemap[ii][jj] = 6
for ii in range(1,33,2):
    for jj in range(1,33,2):
        Gamemap[ii][jj] = blue_map[ii//2][jj//2]
for ii in range(0,33):
    for jj in range(0,33):
        if ii < 17 and jj < 17:
            if Gamemap[ii][jj] == 1 : Gamemap[ii-1][jj] = 5
            elif Gamemap[ii][jj] == 2 : Gamemap[ii][jj-1] = 4
            elif Gamemap[ii][jj] == 3 : Gamemap[ii][jj-1] = 4 ; Gamemap[ii-1][jj] = 5
        if ii > 16 and jj < 17:
            if Gamemap[ii][jj] == 1 : Gamemap[ii][jj-1] = 4 
            elif Gamemap[ii][jj] == 2 : Gamemap[ii+1][jj] = 5 
            elif Gamemap[ii][jj] == 3 : Gamemap[ii][jj-1] = 4 ; Gamemap[ii+1][jj] = 5 
        if ii < 17 and jj > 16:
            if Gamemap[ii][jj] == 1 : Gamemap[ii][jj+1] = 4 
            elif Gamemap[ii][jj] == 2 : Gamemap[ii-1][jj] = 5 
            elif Gamemap[ii][jj] == 3 : Gamemap[ii][jj+1] = 4 ; Gamemap[ii-1][jj] = 5 
        if ii > 16 and jj > 16:
            if Gamemap[ii][jj] == 1 : Gamemap[ii+1][jj] = 5 
            elif Gamemap[ii][jj] == 2 : Gamemap[ii][jj+1] = 4 
            elif Gamemap[ii][jj] == 3 : Gamemap[ii][jj+1] = 4 ; Gamemap[ii+1][jj] = 5
for ii in range(0,33):
    Gamemap[ii][0] = 4
    Gamemap[ii][32] = 4
    Gamemap[0][ii] = 5
    Gamemap[32][ii] = 5
Gamemap_x = np.zeros((17,16), dtype=int); Gamemap_y = np.zeros((16,17), dtype=int)
for ii in range(0,33,2):
    for jj in range(1,33,2):
        Gamemap_x[ii//2][jj//2] = Gamemap[ii][jj]

        Gamemap_y[jj//2][ii//2] = Gamemap[jj][ii]
Gamemap_x[7][7] = 5; Gamemap_x[7][8] = 5; Gamemap_x[9][7] = 5; Gamemap_x[9][8] = 5
Gamemap_y[7][7] = 4; Gamemap_y[7][9] = 4; Gamemap_y[8][7] = 4; Gamemap_y[8][9] = 4

#파이게임 시작
pygame.init()

screen_width = 640
screen_height = 900
darkorchid = (153, 50, 204)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 128)
space_size = 40
GRIDLINECOLOR = (30, 30, 30)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Ricochet game")

background = pygame.image.load("Ricochet_background.png")

rand_array1 = [ii for ii in range(0,15)]
rand_array2 = [ii for ii in range(0,15)]
random.shuffle(rand_array1)
random.shuffle(rand_array2)

character_map = np.zeros((16,16), dtype=int)
character_map[rand_array2[4]][rand_array1[2]] = 1
character_map[rand_array2[8]][rand_array1[6]] = 2
character_map[rand_array2[12]][rand_array1[10]] = 3
character_map[rand_array2[3]][rand_array1[1]] = 4
character_map[rand_array2[7]][rand_array1[5]] = 5

character_red = pygame.image.load("character_red.png")
character_red_size = character_red.get_rect().size
character_red_width = character_red_size[0]
character_red_height = character_red_size[1]
red_y_pos, red_x_pos = np.where(character_map == 1) 
character_red_x_pos = space_size * red_x_pos + 5
character_red_y_pos = space_size * red_y_pos + 5

character_blue = pygame.image.load("character_blue.png")
character_blue_size = character_blue.get_rect().size
character_blue_width = character_blue_size[0]
character_blue_height = character_blue_size[1]
blue_y_pos, blue_x_pos = np.where(character_map == 2)
character_blue_x_pos = space_size * blue_x_pos + 5
character_blue_y_pos = space_size * blue_y_pos + 5

character_brown = pygame.image.load("character_brown.png")
character_brown_size = character_brown.get_rect().size
character_brown_width = character_brown_size[0]
character_brown_height = character_brown_size[1]
brown_y_pos, brown_x_pos = np.where(character_map == 3)
character_brown_x_pos = space_size * brown_x_pos + 5
character_brown_y_pos = space_size * brown_y_pos + 5

character_purple = pygame.image.load("character_purple.png")
character_purple_size = character_red.get_rect().size
character_purple_width = character_purple_size[0]
character_purple_height = character_purple_size[1]
purple_y_pos, purple_x_pos = np.where(character_map == 4)
character_purple_x_pos = space_size * purple_x_pos + 5
character_purple_y_pos = space_size * purple_y_pos + 5

character_black = pygame.image.load("character_black.png")
character_black_size = character_black.get_rect().size
character_black_width = character_black_size[0]
character_black_height = character_black_size[1]
black_y_pos, black_x_pos = np.where(character_map == 5)
character_black_x_pos = space_size * black_x_pos + 5
character_black_y_pos = space_size * black_y_pos + 5

font = pygame.font.Font('Roboto-Black.ttf', 32)
text = font.render('ScoreBoard', True, black)
textRect = text.get_rect()
textRect.center = (320, 700)
#print(character_map)
#print(Gamemap_x)
#print(Gamemap_y)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_x_tran = mouse_x//40 + 1
            mouse_y_tran = mouse_y//40 + 1
            print(mouse_x_tran, mouse_y_tran)
            current_select = character_map[mouse_y_tran-1][mouse_x_tran-1]
            print(current_select)

        if event.type == pygame.KEYDOWN:
            if current_select == 1 or current_select == 2 or current_select == 3 or current_select == 4 or current_select == 5:
                if event.key == pygame.K_LEFT:
                    for ii in range(0,16):
                        if (mouse_x_tran-2-ii) == -1 or character_map[mouse_y_tran-1][mouse_x_tran-2-ii] > 0:
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran-1][mouse_x_tran-1-ii] = current_select
                            break
                        elif Gamemap_y[mouse_y_tran-1][mouse_x_tran-1-ii] == 4 :
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran-1][mouse_x_tran-1-ii] = current_select
                            break
                            
                if event.key == pygame.K_RIGHT:
                    if mouse_x_tran == 16:
                        print("못감")
                        break
                    for ii in range(0,16):
                        if (mouse_x_tran+1+ii) == 16 or character_map[mouse_y_tran-1][mouse_x_tran+1+ii] > 0 :
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran-1][mouse_x_tran+ii] = current_select
                            break
                        if Gamemap_y[mouse_y_tran-1][mouse_x_tran+ii] == 4:
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran-1][mouse_x_tran+ii-1] = current_select
                            break
                    
                if event.key == pygame.K_UP:
                    for ii in range(0,16):
                        if (mouse_y_tran-ii-2) == -1 or character_map[mouse_y_tran-ii-2][mouse_x_tran-1] > 0:
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran-ii-1][mouse_x_tran-1] = current_select
                            break
                        elif Gamemap_x[mouse_y_tran-ii-1][mouse_x_tran-1] == 5:
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran-ii-1][mouse_x_tran-1] = current_select
                            break
                    
                if event.key == pygame.K_DOWN:
                    if mouse_y_tran == 16:
                        print("못감")
                        break
                    for ii in range(0,16):
                        if  (mouse_y_tran+ii+1) == 16 or character_map[mouse_y_tran+ii+1][mouse_x_tran-1] > 0 :
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran+ii][mouse_x_tran-1] = current_select
                            break
                        elif Gamemap_x[mouse_y_tran+ii][mouse_x_tran-1] == 5:
                            character_map[mouse_y_tran-1][mouse_x_tran-1] = 0
                            character_map[mouse_y_tran+ii-1][mouse_x_tran-1] = current_select
                            break
        
        

        

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

    
    screen.fill(white)
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

    pygame.display.update()


pygame.quit()
