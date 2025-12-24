import math
import random 
import pygame 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500 
PLAYER_START_X = 370 
PLAYER_START_Y = 380 
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150 
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40 
BULLET_SPEED_Y = 10 
COLLISION_DISTANCE = 27 
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("OIP (1).webp")
pygame.display.set_icon(icon)
playerImg = pygame.image.load("1000_F_243641810_JCbEXEUCFNkTxg5zhl8pk8DRubr2aJLj.jpg")
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0 
enemylmg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of enemies = 6