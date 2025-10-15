# Compléter ici (noms, groupe, contenu fichier, date)
#
#
#
#
# Ne pas supprimer cette ligne. <trace>sequences_indexation.py</trace>


####################
# Parcours de sous-listes ou sous-chaines, éventuellement avec un pas
####################

# Décommenter et compléter la signature donnée puis faire la suite
def echantillonne(n:int, chaine:str)->str:
    """ renvoie une chaîne contenant un échantillonnage d’un caractère sur n de chaine

    Précondition :n>0
    Exemple(s) :
    $$$ echantillonne(3, 'azertyuiop')
    'arup'
    $$$ echantillonne(1, 'big')
    'big'
    """
    res=chaine[::n]
    return res


# Décommenter et compléter la signature donnée puis faire la suite
def elements_indices_impairs(l:list[int])->list[int]:
    """ envoie une liste contenant les éléments d’indices impairs de l

    Précondition :
    Exemple(s) :
    $$$ elements_indices_impairs([10, 24, 12, 2, 14, 15, 16])
    [24, 2, 15]
    $$$ elements_indices_impairs([2,7,8])
    [7]
    $$$ elements_indices_impairs([])
    []
    """
    res=l[1::2]
    return res

# Décommenter et compléter la signature donnée puis faire la suite
def miroir_pas(chaine:str)->str:
    """ envoie une
    nouvelle chaîne contenant les éléments de chaine dans l’ordre inverse

    Précondition :
    Exemple(s) :
    $$$ miroir_pas('azerty')
    'ytreza'
    $$$ miroir_pas('patpatrouille')
    'elliuortaptap'
    """
    res=chaine[::-1]
    return res
    
    

# Décommenter et compléter la signature donnée puis faire la suite
def minimum(l:list[int])->int:
    """ envoie le plus petit élément de l

    Précondition :
    Exemple(s) :
    $$$ minimum([2])
    2
    $$$ minimum([23,-1,45])
    -1
    $$$ minimum([5,8,32,2])
    2
    """
    min=l[0]
    for elmt in l:
        if elmt<min:
            min=elmt
    return min


####################
# Variable locale à réinitialiser
####################

# Décommenter et compléter la signature donnée puis faire la suite
#def decoupage(chaine, separateurs

####################
# Paires d'éléments consécutifs
####################

# Décommenter et compléter la signature donnée puis faire la suite
#def premieres_occurrences(

####################
# Boucles imbriquées
####################

# Décommenter et compléter la signature donnée puis faire la suite
#def matchs(

####################
# En vrac
####################

# Décommenter et compléter la signature donnée puis faire la suite
#def nom_domaines(extensions, domaines

# Décommenter et compléter la signature donnée puis faire la suite
#def max_identiques(

# Décommenter et compléter la signature donnée puis faire la suite
#def suffixes(

# Décommenter et compléter la signature donnée puis faire la suite
#def resume(

# Décommenter et compléter la signature donnée puis faire la suite
#def ajout_separateur(liste, sep

# Décommenter et compléter la signature donnée puis faire la suite
#def construit_mots(mot1, mot2

########################
# Zorglang
######################

# À vous de jouer !
