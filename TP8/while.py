# Compléter ici (noms, groupe, contenu fichier, date)
#DJEGNON Yves
#GROUPE 12
#PROG TP8
#23/10/2025
# Ne pas supprimer cette ligne. <trace>while.py</trace>


####################
# Utilisation de boucles while
####################

# Décommenter et compléter la signature donnée puis faire la suite
def nb_jours_avant_1m_blob(taille:float)->int:
    """ renvoie le nombre de jours après lesquels le blob atteindra ou dépassera 1 mètre, partant de la taille initiale

    Précondition :/
    Exemple(s) :
    $$$ nb_jours_avant_1m_blob(0.5)
    1
    $$$ nb_jours_avant_1m_blob(0.125)
    3
    $$$ nb_jours_avant_1m_blob(1.92)
    0
    $$$ nb_jours_avant_1m_blob(1)
    0
    """
    res=0
    a=taille
    while a<1:
        a=a*2
        res=res+1
    return res
    

# Décommenter et compléter la signature donnée puis faire la suite
def somme_chiffres(a:int)->int:
    """ renvoie la somme des chiffres du parametre

    Précondition :/
    Exemple(s) :
    $$$ somme_chiffres(123)
    6
    $$$ somme_chiffres(5)
    5
    $$$ somme_chiffres(0)
    0
    """
    res=0
    ent=a
    while ent!=0:
        b=ent%10
        res=res+b
        ent=ent//10
    return res
        
    

# Décommenter et compléter la signature donnée puis faire la suite
def saisie_pseudo_avec_verification(pseudo:str):
    """ renvoie la dernière chaîne saisie

    Précondition :/
    Exemple(s) :/
    """
    a=input('saisir un deuxieme pseudo:')
    res=''
    while a==pseudo:
        a=input('saisir un deuxieme pseudo:')
    return a
        
    
