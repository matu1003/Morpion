import pygame

pygame.font.init()
WIN_W = 999
WIN_H = 999
STAT_FONT = pygame.font.SysFont("arial", 200)

win = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption("Morpion")
win.fill((255, 255, 255))
