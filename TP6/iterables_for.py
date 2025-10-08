# Compléter ici (noms, groupe, contenu fichier, date)
# Djegnon yves
# MI 12
# TP6
#
# Ne pas supprimer cette ligne. <trace>iterables_for.py</trace>


####################
# Algorithmes de traitement de listes
####################

# Décommenter et compléter la signature donnée puis faire la suite
def carres(l:list[int])->list[int]:
    """ renvoie une nouvelle
    liste contenant les carrés des valeurs des éléments de l

    Précondition :\
    Exemple(s) :
    $$$ carres([2, 3, 5, 7])
    [4, 9, 25, 49]
    $$$ carres([4, 3, 0])
    [16, 9, 0]
    """
    l2=[]
    for elemt in l:
        carre=elemt**2
        l2.append(carre)
    return l2
        

# Décommenter et compléter la signature donnée puis faire la suite
def nombre_occurrences(val:int, lentiers:list[int])->int:
    """ renvoie le nombre d’occurrences de la valeur val parmi les éléments de lentiers

    Précondition :
    Exemple(s) :
    $$$ nombre_occurrences(2, [4, 2, 6, 2, 2, 5, 4])
    3
    $$$ nombre_occurrences(7, [4, 2, 6, 2, 2, 5, 4])
    0
    """
    res=0
    for elemt in lentiers:
        if elemt==val:
            res+=1
    return res 

# Décommenter et compléter la signature donnée puis faire la suite
def nombre_occurrences2(a_compter:list[int], liste:list[int])->int:
    """ envoie le nombre d’occurrences cumulé des entiers de a_compter dans
    lentiers.

    Précondition :\
    Exemple(s) :
    $$$ nombre_occurrences2([4, 2, 7], [4, 2, 6, 2, 2, 5, 4])
    5 
    """
    res=0
    for elemt in a_compter:
        res+=nombre_occurrences(elemt,liste)
    return res

# Décommenter et compléter la signature donnée puis faire la suite
def sans_elt(x:int, liste:list[int])->list[int]:
    """ envoie une nouvelle liste contenant les éléments de lentiers dans le même ordre, mais tels que
         les occurrences de x ont été supprimées

    Précondition :\
    Exemple(s) :
    $$$ sans_elt(3, [3, 0, 3, 3, -6, 12, -7, 3])
    [0, -6, 12, -7] 
    """
    l2=[]
    for elemt in liste:
        if x!=elemt:
            l2.append(elemt)
    return l2
    

# Décommenter et compléter la signature donnée puis faire la suite
def moyenne(l:list[int])->float|int:
    """ envoie la moyenne des valeurs de ses élément

    Précondition :l ne doit pas etre vide 
    Exemple(s) :
    $$$ moyenne([2, 3, 5, 7])
    approx(4.25,0.01)
    $$$ moyenne([3,8,10])
    approx(7,0.1)
    """
    somme_note=0
    nbr_note=0
    for elemt in l:
        somme_note+=elemt
        nbr_note+=1
    return somme_note/nbr_note


# Décommenter et compléter la signature donnée puis faire la suite
def concatenation(l_chaine:list[str])->str:
    """ renvoie une chaîne composée de la concaténation des chaînes contenues dans lchaines.    Précondition :
    Exemple(s) :\
    $$$ concatenation(["liste", "de", " chaines"])
    'listede chaines'
    $$$ concatenation(["Bra", "ka", "ta !"])
    'Brakata !'
    """
    res=''
    for c in l_chaine:
        res+=c
    return res

# Décommenter et compléter la signature donnée puis faire la suite
def positive(l:list[int])->list[int]:
    """ renvoie une nouvelle liste contenant les éléments de lentiers dans le même ordre, mais tels que les éléments négatifs
    ont été “positivés” (remplacés par leur opposé)

    Précondition :\
    Exemple(s) :
    $$$ positive([0, 3, -6, 12, -7])
    [0, 3, 6, 12, 7]
    $$$ positive([0, 89, 12, -17])
    [0, 89, 12, 17]
    """
    l2=[]
    for elmt in l:
        if elmt<0:
            res=abs(elmt)
            l2.append(res)
        else:
            l2.append(elmt)
    return l2

# Décommenter et compléter la signature donnée puis faire la suite
def lg_max_chaines(l:list[str])->int:
    """ renvoie la
        longueur de la plus longue chaîne de lchaines 
    Précondition :\
    Exemple(s) :
    $$$ lg_max_chaines(['un', 'milieu max', 'trois'])
    10
    """
    res=0
    for elmt in l:
        if len(elmt)>res:
            res=len(elmt)
    return res
        

####################
# Algorithmes de traitement de chaînes
####################

# Décommenter et compléter la signature donnée puis faire la suite
def chiffres(chaine:str)->str:
    """  renvoie une chaîne contenant
    uniquement les chiffres de chaine, dans le même ordre

    Précondition :\
    Exemple(s) :
    $$$ chiffres('7 et 8 octobre 2023')
    '782023'
    """
    res=''
    for c in chaine:
        if c.isdigit():
            res+=c
    return res

# Décommenter et compléter la signature donnée puis faire la suite
def miroir_for(chaine:str)->str:
    """ renvoie une nouvelle chaîne
    contenant les caractères de chaine dans l’ordre inverse.

    Précondition :
    Exemple(s) :
    $$$ miroir_for("Hello !")
    '! olleH'
    """
    res=''
    for c in chaine:
        res=c+res
    return res

# Décommenter et compléter la signature donnée puis faire la suite
def compte_2car(texte:str, car1:str, car2:str)->int:
    """ renvoie le nombre d’occurrences des caractères car1 et car2
    dans texte.

    Précondition :car1 different de car2
    Exemple(s) :
    $$$ compte_2car('abracadabra', 'a', 'r')
    7
    """
    compte=0
    for c in texte:
        if c==car1 or c==car2:
            compte+=1
    return compte


####################
# Utilisation du type range
####################

# Décommenter et compléter la signature donnée puis faire la suite
def table_multiplication(n:int)->list[int]:
    """ envoie la liste de taille 10 des multiples de n,

    Précondition : n entre 1 et 10 
    Exemple(s) :
    $$$ table_multiplication(5)
    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50] 
    """
    l=[]
    for m in range(1,11):
        multi=m*n
        l.append(multi)
    return l
        
        

# Décommenter et compléter la signature donnée puis faire la suite
def saisie_liste(n:int):
    """ demande la saisie au
clavier de n valeurs entières, avant de retourner la liste associée

    Précondition : n positif ou nu
    Exemple(s) :
    $$$ 
    """
    l=[]
    for i in range(n):
        elmt=int(input('entrer une valeur entiere :'))
        l.append(elmt)
    return l

####################
# Algorithmes qui changent un peu...
####################

# Décommenter et compléter la signature donnée puis faire la suite
def somme_cumulee(l:list[int])->list[int]:
    """ renvoie la liste des sommes cumulées

    Précondition :
    Exemple(s) :
    $$$ somme_cumulee([1, 2, 5])
    [1, 3, 8] 
    """
    res=0
    l2=[]
    for elmt in l:
        res+=elmt
        l2.append(res)
    return l2

# Décommenter et compléter la signature donnée puis faire la suite
def prefixes(chaine:str)->list[str]:
    """ renvoie la liste des préfixes de chaine

    Précondition :
    Exemple(s) :
    $$$ prefixes('motus')
    ['', 'm', 'mo', 'mot', 'motu', 'motus'] 
    """
    l2=['']
    car=''
    for c in chaine:
        car=car+c
        l2.append(car)
    return l2
        

# Décommenter et compléter la signature donnée puis faire la suite
def insere_sauts_ligne(texte:str, lg_ligne:int)->str:
    """ envoie une nouvelle chaîne qui est texte dans laquelle des sauts de ligne (caractère spécial
    '\n') ont été ajoutés après chaque lg_ligne caractères.

    Précondition :
    Exemple(s) :
    $$$ insere_sauts_ligne("Je ne sais pas si des mots seront coupés.", 5)
    "Je ne\\n sais\\n pas \\nsi de\\ns mot\\ns ser\\nont c\\noupés\\n."
    """
    
    texte_saut=""
    compte=0
    for c in texte:
        compte+=1
        if compte%lg_ligne ==0 :
            texte_saut+=f'{c}\n'
        else:
            texte_saut+=c
    return texte_saut
        


##########################
# Écriture d’un programme principal
##########################

def main()->None:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$
    """
    n=int(input('Entrer une longueur de liste :'))
    print('Saisie des 4 valeurs de la liste :')
    liste=saisie_liste(n)
    liste_positive=positive(liste)
    reponse=f'Le résultat de positive({liste}) est : {liste_positive}' 
    print(reponse)


if __name__ == '__main__':
    # éxécuté qd ce module n'est pas initialisé par un import.
    main()