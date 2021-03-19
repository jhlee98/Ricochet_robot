import pygame
import numpy as np
import functions as fn
import random
import sys, os

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


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def rotate_180(mat):
    mat = np.rot90(mat)
    mat = np.rot90(mat)
    return mat
    

def rotate_270(mat):
    mat = np.rot90(mat)
    mat = np.rot90(mat)
    mat = np.rot90(mat)
    return mat


def Createmap():
    map1 = np.zeros((8,8), dtype=int); map2 = np.zeros((8,8), dtype=int); map3 = np.zeros((8,8), dtype=int); map4 = np.zeros((8,8), dtype=int)
    map1_a = np.zeros((8,8), dtype=int); map2_a = np.zeros((8,8), dtype=int); map3_a = np.zeros((8,8), dtype=int); map4_a = np.zeros((8,8), dtype=int)
    map1[0][2] = 3; map1[0][5] = 2; map1[1][5] = 1; map1[3][7] = 2; map1[4][3] = 2; map1[5][2] = 1
    map1[7][1] = 1; map1[6][5] = 1; map1[6][6] = 2
    map1_a[6][6] = 1; map1_a[0][2] = 9; map1_a[5][3] = 13; map1_a[1][5] = 5
    map2[6][0] = 1; map2[5][1] = 2; map2[2][2] = 2; map2[3][2] = 1; map2[7][2] = 1; map2[1][3] = 1
    map2[1][4] = 2; map2[5][6] = 3; map2[2][7] = 2
    map2_a[3][2] = 2; map2_a[6][1] = 6; map2_a[5][6] = 10; map2_a[1][4] = 14
    map3[4][0] = 1; map3[4][1] = 2; map3[7][1] = 1; map3[0][2] = 2; map3[1][2] = 1; map3[6][5] = 3
    map3[1][5] = 1; map3[0][6] = 2; map3[2][7] = 2
    map3_a[4][1] = 3; map3_a[6][5] = 7; map3_a[1][6] = 11; map3_a[1][2] = 15
    map4[3][0] = 2; map4[4][0] = 1; map4[2][1] = 1; map4[1][1] = 2; map4[1][3] = 3; map4[6][3] = 1; map4[6][4] = 2
    map4[7][2] = 1; map4[5][5] = 1; map4[4][6] = 2; map4[2][7] = 2
    map4_a[5][6] = 4; map4_a[6][4] = 8; map4_a[1][3] = 12; map4_a[2][1] = 16
    map1 = map1.T; map2 = map2.T; map3 = map3.T; map4 = map4.T
    map1_a = map1_a.T; map2_a = map2_a.T; map3_a = map3_a.T; map4_a = map4_a.T
    order = [1, 2, 3, 4] ; random.shuffle(order)
    map5 = np.c_[fn.rotate_180(locals()['map{}'.format(order[0])]), np.rot90(locals()['map{}'.format(order[1])])]
    map6 = np.c_[fn.rotate_270(locals()['map{}'.format(order[2])]), locals()['map{}'.format(order[3])]]
    map7 = np.c_[fn.rotate_180(locals()['map{}_a'.format(order[0])]), np.rot90(locals()['map{}_a'.format(order[1])])]
    map8 = np.c_[fn.rotate_270(locals()['map{}_a'.format(order[2])]), locals()['map{}_a'.format(order[3])]]
    blue_map = np.concatenate((map5, map6), axis = 0)
    blue_map_a = np.concatenate((map7, map8), axis = 0)
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
    return blue_map_a, Gamemap_x, Gamemap_y


def Create_character_map():
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
    for ii in range(7, 9):
        for jj in range(7, 9):
            if character_map[ii][jj] != 0:
                character_map[ii+2][jj-2] = character_map[ii][jj]
                character_map[ii][jj] = 0 
    return character_map


def Create_character(img_location, character_map):
    character = pygame.image.load(img_location)
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    y_pos, x_pos = np.where(character_map == 1) 
    character_x_pos = space_size * x_pos + 5
    character_y_pos = space_size * y_pos + 5
    return character, character_x_pos, character_y_pos


def Answer_location(game_order, game_number, blue_map_a):
    if game_order[game_number]<5:
        answer_color = pygame.image.load(resource_path("answer_red.png"))
        answer_size = answer_color.get_rect().size
        answer_width = answer_size[0]
        answer_height = answer_size[1]
        ans_y_pos, ans_x_pos = np.where(blue_map_a == game_order[game_number])
        answer_screen_x_pos = space_size * ans_x_pos 
        answer_screen_y_pos = space_size * ans_y_pos   
    elif game_order[game_number]<9:
        answer_color = pygame.image.load(resource_path("answer_brown.png"))
        answer_size = answer_color.get_rect().size
        answer_width = answer_size[0]
        answer_height = answer_size[1]
        ans_y_pos, ans_x_pos = np.where(blue_map_a == game_order[game_number])
        answer_screen_x_pos = space_size * ans_x_pos 
        answer_screen_y_pos = space_size * ans_y_pos 
    elif game_order[game_number]<13:
        answer_color = pygame.image.load(resource_path("answer_purple.png"))
        answer_size = answer_color.get_rect().size
        answer_width = answer_size[0]
        answer_height = answer_size[1]
        ans_y_pos, ans_x_pos = np.where(blue_map_a == game_order[game_number])
        answer_screen_x_pos = space_size * ans_x_pos 
        answer_screen_y_pos = space_size * ans_y_pos 
    else:
        answer_color = pygame.image.load(resource_path("answer_blue.png"))
        answer_size = answer_color.get_rect().size
        answer_width = answer_size[0]
        answer_height = answer_size[1]
        ans_y_pos, ans_x_pos = np.where(blue_map_a == game_order[game_number])
        answer_screen_x_pos = space_size * ans_x_pos 
        answer_screen_y_pos = space_size * ans_y_pos 
    return answer_color, answer_screen_x_pos, answer_screen_y_pos

