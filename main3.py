import pygame


pygame.font.init()
WIN_W = 666
WIN_H = 666
STAT_FONT = pygame.font.SysFont("arial", 30)
BARRE = 30

win = pygame.display.set_mode((WIN_W, WIN_H+BARRE))
pygame.display.set_caption("Morpion")
win.fill((255, 255, 255))

X = pygame.Surface((WIN_W/3-10, WIN_H/3-10))
X.fill((255, 255, 255))
pygame.draw.line(X, (237,41,57), (0,0), (WIN_W//3-10, WIN_H//3-10), 4)
pygame.draw.line(X, (237,41,57), (WIN_W//3-10,0), (0, WIN_H//3-10), 4)
O = pygame.Surface((WIN_W//3-10, WIN_H/3-10))
O.fill((255, 255, 255))
pygame.draw.circle(O, (80,220,100), (WIN_W//6-5, WIN_H//6-5), WIN_H//6-5, 4)


grille = [["-", "-", "-"] for i in range(3)]
pions = ['X', 'O']
scores = [0, 0]

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


def egalite(grille):
    tie = True
    for ligne in grille:
        for elt in ligne:
            if elt == "-":
                tie = False
    return tie


def minimax(grille, tourIA, nivUn):
    if verifVictoire(grille):
        if tourIA:
            return -1
        else:
            return 1
    if egalite(grille):
        return 0

    eval = []
    eval_score = 2
    if tourIA:
        eval_score = -2

    for ligne in range(3):
        for col in range(3):
            if grille[ligne][col] == "-":
                prediction = [i[:] for i in grille]
                prediction[ligne][col] = pions[int(tourIA)]
                score = minimax(prediction, not(tourIA), False)
                if tourIA and score > eval_score:
                    eval = prediction
                    eval_score = score
                elif not(tourIA) and score < eval_score:
                    eval = prediction
                    eval_score = score
    if nivUn:
        return eval
    else:
        return eval_score


def dess_env():
    score1 = STAT_FONT.render(f"X: {scores[0]}", 1, (237,41,57))
    win.blit(score1, (10, 10))

    score2 = STAT_FONT.render(f"O: {scores[1]}", 1, (80,220,100))
    win.blit(score2, (WIN_W-10-score2.get_width(), 10))

    pygame.draw.line(win, (0,0,0), (WIN_W//3, BARRE), (WIN_W//3, WIN_H+BARRE), 1)
    pygame.draw.line(win, (0,0,0), (2*WIN_W//3, BARRE), (2*WIN_W//3, WIN_H+BARRE), 1)
    pygame.draw.line(win, (0,0,0), (0, WIN_H//3+BARRE), (WIN_W, WIN_H//3+BARRE), 1)
    pygame.draw.line(win, (0,0,0), (0, 2*WIN_H//3+BARRE), (WIN_W, 2*WIN_H//3+BARRE), 1)
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "X":
                win.blit(X, (j*(WIN_W//3)+5, i*(WIN_H//3)+5+BARRE))
            if grille[i][j] == "O":
                win.blit(O, (j*(WIN_W//3)+5, i*(WIN_H//3)+5+BARRE))



continuer = True
clock = pygame.time.Clock()
while continuer:
    game_running = True
    tour = 1
    grille = [["-", "-", "-"] for i in range(3)]
    while game_running:
        clock.tick(1)
        if tour == 1:
            grille = minimax(grille, True, True)
            tour += 1
            tour %= 2
        # elif tour == 0:
        # Pour faire jouer deux IA l une contre l'autre
        #     grille = minimax(grille, False, True)
        #     tour += 1
        #     tour %= 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                continuer = False
                pygame.quit()
                break



            if event.type == pygame.MOUSEBUTTONUP and tour == 0:
                pos = pygame.mouse.get_pos()
                xpos = pos[0]//(WIN_W//3)
                ypos = (pos[1]-BARRE)//(WIN_H//3)
                if grille[ypos][xpos] == "-":
                    grille[ypos][xpos] = pions[tour]
                    tour += 1
                    tour %= 2

        if not(game_running):
            break

        win.fill((255, 255, 255))
        dess_env()
        pygame.display.update()
        if verifVictoire(grille):
            gagnant = (tour+1)%2
            scores[gagnant]+=1
            msg = f"Le joueur {gagnant+1} a gagné!"
            game_running = False
        elif egalite(grille):
            msg = "Egalité!"
            game_running = False


    popup = pygame.Surface((400, 200))
    popup.fill((255, 255, 255))
    pygame.draw.rect(popup, (0,0,0), (3,3,394, 194), 6)

    resultat = STAT_FONT.render(msg, 1, (0,0,255))
    popup.blit(resultat, (200-resultat.get_width()//2, 20))

    recommencer = STAT_FONT.render("Cliquer pour recommencer", 1, (0,0,255))
    popup.blit(recommencer, (200-recommencer.get_width()//2,80))

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                continuer = False
                break
            if event.type == pygame.MOUSEBUTTONUP:
                menu = False
                break

        win.blit(popup, ((WIN_W//2)-200, ((WIN_H//2)-100)))
        pygame.display.update()
