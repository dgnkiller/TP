# Compléter ici (noms, groupe, contenu fichier, date)
# DJEGNON Yves
# MI 12
#
#
# Ne pas supprimer cette ligne. <trace>tictactoe.py</trace>


####################
# Jeu du Tic Tac Toe
####################

JOUEUR1='X'
JOUEUR2='O'

import copy

def afficher_grille(grille: list[list]) -> None:
    """ affiche la grille du tictactoe

    Précondition :
    Exemple(s) :
    $$$
    """   
    for i in range(len(grille)):
        ligne_a_afficher = ""
        for j in range(len(grille[i])):
            ligne_a_afficher += f" {grille[i][j]} "
            
            if j < len(grille[i]) - 1: # pour ne pas mettre de | après la dernière colonne
                ligne_a_afficher += "|"
        
    
        print(ligne_a_afficher)
        
        if i < len(grille) - 1:
            print("---+---+---")

def case_jouable(grille:list[list],l:int,c:int)->bool:
    """ renvoie True si la case de coordonnée l,c est libre

    Précondition :
    Exemple(s) :
    $$$ case_jouable([[' ','X',' '],[' ','X',' ']],0,1)
    False
    $$$ case_jouable([[' ','X',' '],[' ','O',' ']],1,1)
    False
    $$$ case_jouable([[' ','X',' '],[' ','O',' ']],1,0)
    True
    """
    symbole='XO'
    res=True
    if l>len(grille) or c > len(grille[l]) or str(grille[l][c]) in symbole:
        res= False
    return res
        

def saisir_indices(grille:list[list])->tuple:
    """ renvoie les coordonnées de la case à jouer 

    Précondition :
    Exemple(s) :
    $$$
    """
    while True:
        try:
            
            saisie = int(input("Entrez le numéro de la case à jouer : "))
            if 1<= saisie and saisie<= 9:
                ligne = (saisie - 1) // 3
                colonne = (saisie - 1) % 3
                if case_jouable(grille,ligne,colonne):
                    return ligne, colonne
                else:
                    print("Cette case n'est pas jouable ! Essayez un autre")
            else:
                print("Le numéro decase doit etre compris entre 1 et 9")
        except ValueError:
            print("Veuillez entrer un CHIFFRE ENTIER")

def affiche_joueur_courant(joueur:str)->None:
    """ affiche un message indiquant quel joueur doit jouer

    Précondition :
    Exemple(s) :
    $$$
    """
    print(f"--- C'est le tour du joueur {joueur} ---")
    
def jouer_coup(grille: list[list], ligne: int, colonne: int, symbole: str) ->list[list]:
    """ pose le pion jouer

    Précondition :
    Exemple(s) :
    $$$
    """
    grille[ligne][colonne]=symbole
def changer_joueur(joueur:str)->str:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$
    """
    if joueur == JOUEUR1:
        return JOUEUR2
    else:
        return JOUEUR1
    
def victoire(grille:list[list],symbole:str)->bool:
    """ renvoie true si le joueur utilisant symbole a gagné

    Précondition :
    Exemple(s) :
    $$$
    """
    # verification des ligne
    for i in range(len(grille)):
        if grille[i][0] == symbole and grille[i][1] == symbole and grille[i][2] == symbole:
            return True
    # verification des colonnes
    for j in range(len(grille[0])):
        if grille[0][j] == symbole and grille[1][j] == symbole and grille[2][j] == symbole:
            return True
    # verification diagonale gauche > droite
    if grille[0][0] == symbole and grille[1][1] == symbole and grille[2][2] == symbole:
        return True
    # verification diagonale droite> gauche
    elif grille[0][2] == symbole and grille[1][1] == symbole and grille[2][0] == symbole:
        return True
    else:
        return False
    
def match_nul(grille: list[list]) -> bool:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$
    """
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            
            if str(grille[i][j]) not in 'XO':
                return False
                
   
    return True
    

def jouer() -> None:
    """Fonction principale.
    """
    grille=[[1,2,3],[4,5,6],[7,8,9]]
    joueur=JOUEUR1
    jeu_en_cours=True
    print("--- BIENVENU DANS LE JEU TIC-TAC-TOE ---")
#
    ### boucle de jeu
    while jeu_en_cours :
        afficher_grille(grille)
        affiche_joueur_courant(joueur)
        l,c=saisir_indices(grille)       
        jouer_coup(grille,l,c,joueur)
        if victoire(grille,joueur):
            afficher_grille(grille)
            print(f"BRAVO ! Le joueur {joueur} a gagné !")
            jeu_en_cours = False
        elif match_nul(grille):
            afficher_grille(grille)
            print("Match nul ! La grille est pleine.")
            jeu_en_cours=False
        else:
            joueur= changer_joueur(joueur)

