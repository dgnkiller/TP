# Compléter ici (noms, groupe, contenu fichier, date)
#DJEGNON Yves
#GP12
#PROG TP8
#23/10/2025
# Ne pas supprimer cette ligne. <trace>jeu_nim.py</trace>


####################
# Jeu de Nim
####################

# Décommenter et compléter la signature donnée puis faire la suite
def saisie_nom()->str:
    """ saisir les noms de joueurs

    Précondition :/
    Exemple(s) : 
    """
    a=input('Donner un nom de joueur:')
    return a
    
    
    

# Décommenter et compléter la signature donnée puis faire la suite
def saisie_nom_different(a:str)->str:
    """ saisir un nom different

    Précondition :
    Exemple(s) :
    $$$ 
    """
    b=input('Donner un nom de joueur :')
    while b==a:
        print(f'Le nom {a}  existe déjà')
        b=input('Donner un nom de joueur :')
    return b
        
        

# Décommenter et compléter la signature donnée puis faire la suite
def max_possible_a_prendre(a:int)->bool:
    """ affiche le nobre d'allumette restante apres avoir pris

    Précondition :/
    Exemple(s) :
    $$$ max_possible_a_prendre(2)
    True
    $$$ max_possible_a_prendre(4)
    False
    """
    return 1<=a<=3
        
        
        
    

# Décommenter et compléter la signature donnée puis faire la suite
def saisir_nb_allumettes_prises()->str:
    """ saisi le nbre dallumettes prises

    Précondition :/
    Exemple(s) : 
    """
    c=input("Combien d'allumettes prenez-vous?:")
    return c
    
    

#Décommenter et compléter la signature donnée puis faire la suite
def indice_autre_joueur(i:int)->int:
    """ gérer le nom des joueurs et le calcul du changement de joueur courant,

    Précondition :/ 
    Exemple(s) :/ 
    """
    return 1-i
        
# Décommenter et compléter la signature donnée puis faire la suite
def jouer()->None:
    #### Initialisation de l'état du jeu
     #nombre d'allumettes
    nb_allumettes=16
    # Saisie du nom du 1er joueur
    a=saisie_nom()
    # Saisie du nom du 2nd joueur, différentdu 1er
    b=saisie_nom_different(a)
    print('nb allumettes : 16') 
    # Définition du tableau contenant les joueurs
    joueur=[a,b]
    # Tirage au sort de l'indice dans ce tableau du joueur
    from random import randint
    i=randint(0,1)
    # courant
    j=indice_autre_joueur(i)
    print(f'{joueur[j]} :à vous !')
    #### Boucle de jeu
    while nb_allumettes>0:
        # affichage du nombre d'allumettes
        c=int(saisir_nb_allumettes_prises())
        if not(max_possible_a_prendre(c)):
            print("Le nombre saisi n'est pas conforme.")
        else: 
            nb_allumettes=nb_allumettes-c
            j=indice_autre_joueur(i)
            if nb_allumettes!=0:
                print(f'nb allumettes : {nb_allumettes}')
                i=1-i
                print(f'{joueur[j]} :à vous !')
            if nb_allumettes==0:
                 print(f"Plus d'allumettes !{joueur[j-1]}  a gagné !")      
if __name__ == '__main__':
     jouer()
    # éxécuté qd ce module n'est pas initialisé par un import.
    # compléter par un appel à la fonction principale
