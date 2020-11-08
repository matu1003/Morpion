
def afficherGrille(grille):
    #Fonction qui affiche l'etat actuel de la grille
    print("  1   2   3")
    lignes = "ABC"
    for ligne in range(len(grille)):
        #Affiche une ligne avec separation entre colonnes
        contenu = lignes[ligne]+ " " + " | ".join(grille[ligne])
        print(contenu)
        if ligne == 0 or ligne == 1:
            #Entre les lignes 1/2 et 2/3,
            #on met des pointillets pour separer les lignes
            print("  "+"-"*(len(contenu)-2))

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
colonnes = ["1", "2", "3"]
lignes = ["A", "B", "C"]

afficherGrille(grille)
print("Joueur 1: X")
print("Joueur 2: O")
partie_en_cours = True
while partie_en_cours:
    print(f"Au joueur {tour+1}:")
    case = ""
    conditions_fausses = True
    while conditions_fausses:
        case = input("Entrez votre case (ligne puis colonne): ")
        if len(case) == 2:
            if case[0] in lignes and case[1] in colonnes:
                colonne = int(case[1])-1
                ligne = lignes.index(case[0])
                if grille[ligne][colonne] == "-":
                    grille[ligne][colonne] = pions[tour]
                    conditions_fausses = False
                else:
                    print("Case occupée")
            else:
                print("Case invalide")
        else:
            print("Format invalide")


    afficherGrille(grille)
    if verifVictoire(grille):
        partie_en_cours = False
    else:
        tour += 1
        tour %= 2


print(f"Le joueur {tour+1} a gagné!")
