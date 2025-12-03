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
    g=[]
    for _ in range(l):
        ligne=[" "]*c
        g.append(ligne)
    return g

def afficher_grille(grille: list[list]) -> None:
    """ affiche la grille du puissance 4

    Précondition :
    Exemple(s) :
    $$$
    """
    nb_col=len(grille[0])
    
    entete=""
    for k in range(nb_col):
        entete+=f" {k+1}  "
    print(entete)
    
    for i in range(len(grille)):
        ligne_a_afficher = ""
        for j in range(len(grille[i])):
            ligne_a_afficher += f" {grille[i][j]} "
            
            if j < nb_col - 1: # pour ne pas mettre de | après la dernière colonne
                ligne_a_afficher += "|"
        
    
        print(ligne_a_afficher)
        
        if i < len(grille) - 1:
            ligne_sep="---+"*nb_col
            print(ligne_sep[:-1])
            
