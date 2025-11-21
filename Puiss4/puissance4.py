# Compléter ici (noms, groupe, contenu fichier, date)
# DJEGNON Yves
# MI 12
#
#
# Ne pas supprimer cette ligne. <trace>puissance4.py</trace>


####################
# Jeu du Puissance4
####################

def creer_grille(l:int,c:int)->list[list]:
    """ creer une grille de c colonne et l ligne

    Précondition :
    Exemple(s) :
    $$$ 
    """
    g=[None]*l
    for k in range(l):
        g[k]=[' ']*c
    return g

def afficher_grille(grille: list[list]) -> None:
    """ affiche la grille du puissance 4

    Précondition :
    Exemple(s) :
    $$$
    """   
    print(" 1   2   3   4   5   6   7")
    for i in range(len(grille)):
        ligne_a_afficher = ""
        for j in range(len(grille[i])):
            ligne_a_afficher += f" {grille[i][j]} "
            
            if j < len(grille[i]) - 1: # pour ne pas mettre de | après la dernière colonne
                ligne_a_afficher += "|"
        
    
        print(ligne_a_afficher)
        
        if i < len(grille) - 1:
            str="---+"*7
            print(str[:len(str)-1])
            
