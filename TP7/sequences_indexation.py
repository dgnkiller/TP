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

    Précondition :l non vide
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
def decoupage(chaine:str, separateurs:str)->list[str]:
    """ renvoie la liste des mots de texte séparés au niveau d’un des caractères contenu dans separateurs

    Précondition :
    Exemple(s) :
    $$$ decoupage('Tu as fini tes devoirs ? Non, pas encore.', ',.; !?')
    ['Tu', 'as', 'fini', 'tes', 'devoirs', '', '', 'Non', '', 'pas', 'encore']
    """
    ch1=''
    l=[]
    for c in chaine:
        if c in separateurs:
            l.append(ch1)
            ch1=''
        else:
            ch1=ch1+c
    
    return l

####################
# Paires d'éléments consécutifs
####################

# Décommenter et compléter la signature donnée puis faire la suite
def premieres_occurrences(chaine:str)->str:
    """envoie une chaîne de caractères contenant uniquement la première occurrence en cas d’occurrences
    consécutives.
    Précondition :
    Exemple(s) :
    $$$ premieres_occurrences("aabbbaabcdd")
    'ababcd'
    $$$ premieres_occurrences("biiggybo")
    "bigybo"
    """
    res=''
    elmt_precedent=chaine[0]
    for c in chaine[1:]:
        if not c==elmt_precedent:
            res+=c
        elmt_precedent=c
    return chaine[0]+res

####################
# Boucles imbriquées
####################

# Décommenter et compléter la signature donnée puis faire la suite
def matchs(liste1:list[str],liste2:list[str])->list[tuple[str,str]]:
    """renvoie une liste de tous les couples d'element de liste1 et liste2

    Précondition :
    Exemple(s) :
    $$$ matchs(['Losc', 'RC Lens'], ['Stade Rennais', 'FC Lorient', 'Stade Brestois'])
    [('Losc', 'Stade Rennais'), \
    ('Losc', 'FC Lorient'), \
    ('Losc', 'Stade Brestois'), \
    ('RC Lens', 'Stade Rennais'), \
    ('RC Lens', 'FC Lorient'), \
    ('RC Lens', 'Stade Brestois')]
    """
    liste3=[]
    for i in liste1:
        for j in liste2:
            res=(i,j)
            liste3.append(res)
    return liste3
    

####################
# En vrac
####################

# Décommenter et compléter la signature donnée puis faire la suite
def nom_domaines(extensions:list[str], domaines:list[str])->list[str]:
    """ renvoie la liste des noms de domaines pour
    le sous-domaine www.

    Précondition :
    Exemple(s) :
    $$$ nom_domaines(['fr', 'net', 'eu'], ['mondomaine', 'mon_domaine_a_moi'])
    ['www.mondomaine.fr',\
     'www.mondomaine.net',\
     'www.mondomaine.eu',\
     'www.mon_domaine_a_moi.fr',\
     'www.mon_domaine_a_moi.net',\
     'www.mon_domaine_a_moi.eu']
    """
    liste=[]
    sous_domaine='www.'
    for elmt in domaines:
        for ext in extensions:
            res=elmt+'.'+ext
            nom=sous_domaine+res
            liste.append(nom)
    return liste
            
            

# Décommenter et compléter la signature donnée puis faire la suite
def max_identiques(l:list[int])->int:
    """ renvoie le nombre maximum d’éléments consécutifs identiques.
    Précondition :
    Exemple(s) :
    $$$ max_identiques([1, 2, 2, 2, 1, 6, 6, 5])
    3  
    """
    compt=0
    elmt_preced=l[0]
    for elmt in l[1:]:
        if elmt==elmt_preced:
            compt+=1
        elmt_preced=elmt
         
    return compt
       

# Décommenter et compléter la signature donnée puis faire la suite
def suffixes(chaine:str)->list[str]:
    """ renvoie la liste des suffixes de chaine

    Précondition :
    Exemple(s) :
    $$$ suffixes('fin')
    ['', 'n', 'in', 'fin'] 
    """
    l=[]
    res=''
    for c in chaine:
        
# Décommenter et compléter la signature donnée puis faire la suite
#def resume(

# Décommenter et compléter la signature donnée puis faire la suite
#def ajout_separateur(liste, sep

# Décommenter et compléter la signature donnée puis faire la suite
#def construit_mots(mot1, mot2

########################
# Zorglang
######################

