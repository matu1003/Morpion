import pygame

pygame.font.init()
WIN_W = 666
WIN_H = 666
STAT_FONT = pygame.font.SysFont("arial", 200)

win = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption("Morpion")
win.fill((255, 255, 255))

X = pygame.Surface((WIN_W/3-10, WIN_H/3-10))
X.fill((255, 255, 255))
pygame.draw.line(X, (0,0,0), (0,0), (WIN_W//3-10, WIN_H//3-10), 2)
pygame.draw.line(X, (0,0,0), (WIN_W//3-10,0), (0, WIN_H//3-10), 2)
O = pygame.Surface((WIN_W//3-10, WIN_H/3-10))
O.fill((255, 255, 255))
pygame.draw.circle(O, (0,0,0), (WIN_W//6-5, WIN_H//6-5), WIN_H//6-5, 2)


grille = [["-", "-", "-"] for i in range(3)]

def verifVictoire(grille):
    #Check Lignes:
    for ligne in grille:
        if ligne[0] == ligne[1] and ligne[1] == ligne[2] and ligne[0] != "-":
            return True

    #Check colonne:
    for colonne in range(3):
        if grille[0][colonne] == grille[1][colonne] and grille[1][colonne] == grille[2][colonne] and grille[2][colonne] != "-":
            return True

    #Check Diagos:
    #Diago Haut Gauche a Bas Droit
    if grille[0][0] == grille[1][1] and grille[1][1] == grille[2][2] and grille[2][2] != "-":
        return True

    #Diago Haut Droite a Bas Gauche
    if grille[0][2] == grille[1][1] and grille[1][1] == grille[2][0] and grille[2][0] != "-":
        return True

    #Si aucune état terminal n'est atteint:
    return False

def dess_env():
    pygame.draw.line(win, (0,0,0), (WIN_W//3, 0), (WIN_W//3, WIN_H), 1)
    pygame.draw.line(win, (0,0,0), (2*WIN_W//3, 0), (2*WIN_W//3, WIN_H), 1)
    pygame.draw.line(win, (0,0,0), (0, WIN_H//3), (WIN_W, WIN_H//3), 1)
    pygame.draw.line(win, (0,0,0), (0, 2*WIN_H//3), (WIN_W, 2*WIN_H//3), 1)
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "X":
                win.blit(X, (j*(WIN_W//3)+5, i*(WIN_H//3)+5))
            if grille[i][j] == "O":
                win.blit(O, (j*(WIN_W//3)+5, i*(WIN_H//3)+5))

game_running = True
tour = 0
pions = ['X', 'O']
clock = pygame.time.Clock()
while game_running:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            break
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            xpos = pos[0]//(WIN_W//3)
            ypos = pos[1]//(WIN_H//3)
            grille[ypos][xpos] = pions[tour]
            tour += 1
            tour %= 2


    win.fill((255, 255, 255))
    dess_env()
    pygame.display.update()
    if verifVictoire(grille):
        game_running = False
