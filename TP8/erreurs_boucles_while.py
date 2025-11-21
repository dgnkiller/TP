# L1 MI S1 - Prog
# TP exos de manipulation - semaine 8
# oct 2023

def multiplication(a:int, b:int):
    """Renvoie le résultat de a * b en utilisant des additions.

    Précondition : a et b positifs
    Exemple(s) :
    $$$ multiplication(0, 0)
    0
    $$$ multiplication(1, 10)
    10
    $$$ multiplication(3, 6)
    18
    $$$ multiplication(9, 5)
    45
    """
    res = 0
    i = b
    while i >= 0:
        i = i - 1
        res = res + a
    return res

def saisie_reponse() -> str:
    """Demande à l'utilisateur une réponse qui est
    soit 'y' soit 'n'.
    """
    saisie_correcte = True
    while not saisie_correcte:
        reponse = input('Oui ou non ? [y/n] :')
        saisie_correcte = (len(reponse) == 1 and reponse in 'yn')
    return reponse

def duree_atteinte_seuil(cas_init:int, seuil:int):
    """Renvoie le nombre de jours pour atteindre le seuil en partant de
    cas_init cas initiaux, si une population triple tous les 5 jours
    
    Précondition : cas_init > 0 et seuil >=0
    Exemple(s) :
    $$$ duree_atteinte_seuil(1, 0)
    0
    $$$ duree_atteinte_seuil(100, 300)
    5
    $$$ duree_atteinte_seuil(100, 900)
    10
    $$$ duree_atteinte_seuil(100, 950)
    15
    """
    jours = 0
    while cas < seuil:
        jours = jours + 5
        cas = cas * 3
    return jours

def compte_elements_identiques(liste1:list[int], liste2:list[int]) -> int:
    """Renvoie le nb d'éléments identiques et au même indice
    dans liste1 et liste2

    Précondition : len(liste1) = len(liste2)
    Exemple(s) :
    $$$ compte_elements_identiques([1, 3, 4, 5], [1, 5, 4, 6])
    2
    $$$ compte_elements_identiques([], [])
    0
    $$$ compte_elements_identiques([1, 2, 3], [4, 5, 6])
    0
    """
    i = 0
    cpt = 0
    while i < len(liste1):
        if liste1[i] == liste2[i]:
           cpt = cpt + 1
    return cpt
   
def racine_entiere(n:int)->int:
    """Renvoie la racine entière de l'entier n passé en paramètre

    Précondition : n > 0
    Exemple(s) :
    $$$ racine_entiere(0)
    0
    $$$ racine_entiere(1)
    1
    $$$ racine_entiere(4)
    2
    $$$ racine_entiere(10)
    3
    """
    racine = 0
    carre = racine ** 2
    while carre <= n:
        carre = racine ** 2
    return racine - 1

 


