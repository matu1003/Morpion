def afficherGrille(grille):
    #Fonction qui affiche l'etat actuel de la grille
    for ligne in range(len(grille)):
        #Affiche une ligne avec separation entre colonnes
        contenu = " | ".join(grille[ligne])
        print(contenu)
        if ligne == 0 or ligne == 1:
            #Entre les lignes 1/2 et 2/3,
            #on met des pointillets pour separer les lignes
            print("-"*len(contenu))

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



grille = [["-", "-", "-"] for i in range(3)]
tour = 0
pions = ["X", "O"]
afficherGrille(grille)
print("Joueur 1: X")
print("Joueur 2: O")
while True:
    print(f"Au joueur {tour+1}:")
    col = int(input("Colonne: ")) -1
    ligne = int(input("Ligne: ")) -1
    grille[ligne][col] = pions[tour]
    afficherGrille(grille)
    tour += 1
    tour %= 2
    if verifVictoire(grille):
        break
