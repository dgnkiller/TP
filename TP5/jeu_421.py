# Compléter ici (noms, groupe, contenu fichier, date)
# DJEGNON Yves
# MI 12
# 3/10/25
# TP5
# Ne pas supprimer cette ligne. <trace>jeu_421.py</trace>

####### fonctions d'affichage

def affiche_congratulation(a,b,c)->None:
    """ affiche un message de congratulation

    Précondition :
    Exemple(s) :
    $$$ 
    """
    print(f"Felicitation {a},{b},{c} est gagnant")
    

def affiche_perdant(a,b,c)->None:
    """ affiche le message quand on perd

    Précondition :
    Exemple(s) :
    $$$ 
    """
    print(f"pas de chance : {a}, {b}, {c} est perdant")

def affiche_presentation_jeu(nom)->None:
    """ affiche un message de presentation du jeu 421

    Précondition :
    Exemple(s) :
    $$$ 
    """
    print(f"{nom}, bienvenue au jeu du 421 ! \nLancez les dés et tentez d'obtenir 421.")
    

def affiche_lancer(a,b,c)->None:
    """ affiche le resultat du lancer de dés

    Précondition :
    Exemple(s) :
    $$$ 
    """
    l1="+---+ +---+ +---+"
    l2=f"| {a} | | {b} | | {c} |"
    l3="+---+ +---+ +---+"
    print(l1)
    print(l2)
    print(l3)

####### fonctions de saisie

def saisie_continuation()->str:
    """ renvoie y ou n et affiche le message `Souhaitez-vous tenter
    votre chance ? y/n :'

    Précondition :
    Exemple(s) :
    $$$ 
    """
    return input("Souhaitez-vous tenter votre chance ? y/n :" )
    

def saisie_pseudo()->str:
    """ renvoie le pseudo du joueur et affiche le message 'Entrez votre pseudo : '


    Précondition :
    Exemple(s) :
    $$$ 
    """
    return input("Entrez votre pseudo : ")
    

####### fonctions de calcul
from random import randint
# Décommenter et compléter la signature donnée puis faire la suite
def lancer_de()->int:
    """  Simule le lancer de 3 dé à 6 faces

    Précondition :
    Exemple(s) :
    $$$ 
    """
    d= randint(1,6)
    return d
    
# Décommenter et compléter la signature donnée puis faire la suite
def est_42(de1,de2):
    """ renvoie true si le 2 de forme 42

    Précondition :
    Exemple(s) :
    $$$ est_42(2,5)
    False
    est_42(2,4)
    True
    """
    return (de1==4 and de2==2) or (de1==2 and de2==4)
def est_421(de1:int,de2:int,de3:int)->bool:
    """ renvoie True ssi 3 valeurs issues de 3 lancer de dé forment un 421 éventuellement dans le désordre

    Précondition :les valeurs des parametre sont des resultats de lancer de dé 
    Exemple(s) :
    $$$ est_421(2,5,6)
    False
    $$$ est_421(1,4,2)
    True
    $$$ est_421(4,2,1)
    True
    """
    if est_42(de1,de2):
        res= de3==1
    elif est_42(de1,de3):
        res= de2==1
    elif est_42(de2,de3):
        res= de1==1
    else:
        return False
    return res
        

# Décommenter et compléter la signature donnée puis faire la suite
#def veut_continuer(

###### programme principal


